from .models import CourseDocuments, Assignment, StudentAssignment, Forum, ForumReply, Quiz, QuestionBank, Topics, Question, StudentGrades

def get_course_documents(course):
    """
    Return all documents and videos for a course.
    """
    return CourseDocuments.objects.filter(course_id=course).order_by('-upload_time')

def get_course_assignments(course):
    """
    Return all assignments for a course.
    """
    return Assignment.objects.filter(course_id=course).order_by('-upload_time')

def get_student_assignments(assignment):
    """
    Return all student submissions for an assignment.
    """
    return StudentAssignment.objects.filter(assignment_id=assignment)

def get_student_assignment(student, assignment):
    """
    Return specific assignment submission for a student.
    """
    return StudentAssignment.objects.filter(student_id=student, assignment_id=assignment).first()

def get_course_forum(course):
    """
    Return all root forum posts for a course.
    """
    replies = ForumReply.objects.all().values_list('forum_reply_id', flat=True)
    return Forum.objects.filter(course_id=course).exclude(id__in=replies).order_by('-comment_time')

def get_forum_replies(forum_post):
    """
    Return replies for a specific forum post.
    """
    return ForumReply.objects.filter(reply_info=forum_post).select_related('forum_reply')

def get_course_quizzes(course):
    """
    Return all quizzes for a course.
    """
    return Quiz.objects.filter(course_id=course).order_by('-start_time')

def get_active_quizzes(course, current_time):
    """
    Return active quizzes.
    """
    return Quiz.objects.filter(
        course_id=course,
        start_time__lte=current_time,
        end_time__gte=current_time
    )

def get_course_question_banks(course):
    """
    Return question banks for a course.
    """
    return QuestionBank.objects.filter(course_id=course)

def get_quiz_questions(quiz):
    """
    Return questions of a quiz.
    """
    from .models import QuizQuestion
    return QuizQuestion.objects.filter(quiz_id=quiz).select_related('question')

def get_student_grades(student, course):
    """
    Return grades for a student in a specific course.
    """
    return StudentGrades.objects.filter(student_id=student, course_id=course)
