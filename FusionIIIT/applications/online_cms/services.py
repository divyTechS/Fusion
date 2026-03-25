from applications.academic_information.models import Curriculum, Curriculum_Instructor, Student, Course, Student_attendance
from applications.academic_procedures.models import Register
from applications.globals.models import ExtraInfo
from .models import (Assignment, StudentAssignment, CourseDocuments,
                     Forum, ForumReply, Quiz, QuizQuestion, StudentAnswer,
                     QuizResult, GradingScheme, StudentEvaluation)
import datetime

def get_extra_info(user):
    return ExtraInfo.objects.filter(user=user).first()

def is_student(extra_info):
    return Student.objects.filter(id=extra_info).exists()

def get_courses_for_user(user):
    extra_info = get_extra_info(user)
    if not extra_info:
        return []
    student = Student.objects.filter(id=extra_info).first()
    seen = set()
    result = []
    if student:
        registers = Register.objects.filter(student_id=student).select_related(
            'curr_id', 'curr_id__course_id').order_by('curr_id__course_code')
        curriculums = [r.curr_id for r in registers]
    else:
        instructor_links = Curriculum_Instructor.objects.filter(
            instructor_id=extra_info).select_related(
            'curriculum_id', 'curriculum_id__course_id').order_by(
            'curriculum_id__course_code')
        curriculums = [link.curriculum_id for link in instructor_links]
    for curr in curriculums:
        if not curr or curr.course_code in seen:
            continue
        seen.add(curr.course_code)
        result.append({
            'courseCode': curr.course_code,
            'courseName': curr.course_id.course_name,
            'semester': curr.sem,
            'credits': curr.credits,
        })
    return result

def get_course_obj(course_code):
    curr = Curriculum.objects.select_related('course_id').filter(
        course_code=course_code).first()
    return curr

def is_enrolled(user, course_code):
    extra_info = get_extra_info(user)
    if not extra_info:
        return False
    student = Student.objects.filter(id=extra_info).first()
    if student:
        return Register.objects.filter(
            student_id=student,
            curr_id__course_code=course_code).exists()
    return Curriculum_Instructor.objects.filter(
        instructor_id=extra_info,
        curriculum_id__course_code=course_code).exists()


def get_course_roster(course_code):
    """Return enrolled students for a curriculum/course_code.

    Output items:
      { "student_id": "23BCS001", "name": "Full Name" }
    """
    regs = Register.objects.filter(curr_id__course_code=course_code).select_related(
        'student_id', 'student_id__id', 'student_id__id__user'
    )
    res = []
    seen = set()
    for r in regs:
        s = r.student_id
        if not s or not getattr(s, 'id', None) or not getattr(s.id, 'user', None):
            continue
        username = s.id.user.username
        if username in seen:
            continue
        seen.add(username)
        res.append({
            'student_id': username,
            'name': s.id.user.get_full_name() or username,
        })
    return res


def get_instructor_link(extra_info, course_code):
    """Return Curriculum_Instructor row for this faculty+course_code (or None)."""
    return Curriculum_Instructor.objects.filter(
        instructor_id=extra_info,
        curriculum_id__course_code=course_code,
    ).select_related('curriculum_id').first()
