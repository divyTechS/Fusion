from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction

from applications.globals.models import ExtraInfo, Faculty, DepartmentInfo
from applications.academic_information.models import Course, Curriculum, Curriculum_Instructor, Student
from applications.academic_procedures.models import Register


class Command(BaseCommand):
    help = "Seed demo data for Online CMS (faculty + CSE courses + enrollment + passwords)."

    @transaction.atomic
    def handle(self, *args, **options):
        demo_password = "Fusion@2024"

        # --- Ensure student exists and reset password ---
        student_username = "23BCS001"
        try:
            student_user = User.objects.get(username=student_username)
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Student user '{student_username}' not found"))
            return

        student_user.set_password(demo_password)
        student_user.save(update_fields=["password"])

        student_extrainfo = ExtraInfo.objects.filter(user=student_user).first()
        if not student_extrainfo:
            self.stderr.write(self.style.ERROR(f"ExtraInfo missing for '{student_username}'"))
            return

        student_obj = Student.objects.filter(id=student_extrainfo).first()
        if not student_obj:
            self.stderr.write(self.style.ERROR(f"Student row missing for '{student_username}'"))
            return

        # --- Create faculty user + profile (Prof. Ashok) ---
        faculty_username = "ashok"
        faculty_user, created = User.objects.get_or_create(
            username=faculty_username,
            defaults={
                "first_name": "Ashok",
                "last_name": "",
                "email": "ashok@iiitdmj.ac.in",
                "is_staff": True,
                "is_active": True,
            },
        )
        if not created:
            # keep existing names/email if already there
            pass

        faculty_user.set_password(demo_password)
        faculty_user.save()

        department = DepartmentInfo.objects.filter(name__iexact="CSE").first() or DepartmentInfo.objects.first()

        faculty_extrainfo, _ = ExtraInfo.objects.get_or_create(
            user=faculty_user,
            defaults={
                "id": faculty_username,
                "title": "Dr.",
                "sex": "M",
                "user_status": "PRESENT",
                "address": "",
                "phone_no": 9999999999,
                "user_type": "staff",
                "department": department,
                "about_me": "Professor Ashok (demo)",
            },
        )

        # Ensure faculty model exists
        Faculty.objects.get_or_create(id=faculty_extrainfo)

        # --- Create demo courses and assign instructor + enroll student ---
        demo_courses = [
            ("CS101", "Introduction to Programming", "Basics of programming in Python, problem solving."),
            ("CS102", "Data Structures", "Arrays, stacks, queues, linked lists, trees, graphs."),
            ("CS201", "Database Systems", "Relational model, SQL, normalization, transactions."),
        ]

        programme = "B.Tech"
        branch = "CSE"
        batch = 2023
        sem = 1
        credits = 4
        course_type = "Professional Core"

        created_curr = 0
        for course_code, course_name, course_details in demo_courses:
            course, _ = Course.objects.get_or_create(
                course_name=course_name,
                defaults={"course_details": course_details},
            )
            if course.course_details != course_details:
                course.course_details = course_details
                course.save(update_fields=["course_details"])

            curr, was_created = Curriculum.objects.get_or_create(
                course_code=course_code,
                batch=batch,
                programme=programme,
                defaults={
                    "course_id": course,
                    "credits": credits,
                    "course_type": course_type,
                    "branch": branch,
                    "sem": sem,
                    "optional": False,
                    "floated": True,
                },
            )
            if not was_created:
                # keep it consistent with demo values
                changed = False
                if curr.course_id_id != course.id:
                    curr.course_id = course
                    changed = True
                if curr.branch != branch:
                    curr.branch = branch
                    changed = True
                if curr.sem != sem:
                    curr.sem = sem
                    changed = True
                if curr.credits != credits:
                    curr.credits = credits
                    changed = True
                if curr.course_type != course_type:
                    curr.course_type = course_type
                    changed = True
                if not curr.floated:
                    curr.floated = True
                    changed = True
                if changed:
                    curr.save()
            else:
                created_curr += 1

            Curriculum_Instructor.objects.get_or_create(
                curriculum_id=curr,
                instructor_id=faculty_extrainfo,
                defaults={"chief_inst": True},
            )

            Register.objects.get_or_create(
                curr_id=curr,
                student_id=student_obj,
                defaults={"semester": sem},
            )

        self.stdout.write(self.style.SUCCESS("Seeded Online CMS demo data"))
        self.stdout.write(self.style.SUCCESS(f"Student login: {student_username} / {demo_password}"))
        self.stdout.write(self.style.SUCCESS(f"Faculty login: {faculty_username} / {demo_password}"))
        self.stdout.write(self.style.SUCCESS(f"Created {created_curr} new Curriculum entries"))
