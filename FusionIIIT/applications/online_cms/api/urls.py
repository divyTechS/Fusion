from django.urls import path
from . import views

app_name = 'online_cms'

urlpatterns = [
    path('api/courses/', views.ApiCourseList.as_view(), name='api_courses'),
    path('api/<str:course_code>/dashboard/', views.ApiCourseDashboard.as_view(), name='api_dashboard'),
    path('api/<str:course_code>/assignments/', views.ApiAssignments.as_view(), name='api_assignments'),
    path('api/<str:course_code>/assignments/add/', views.ApiAddAssignment.as_view(), name='api_add_assignment'),
    path('api/<str:course_code>/assignments/upload/', views.ApiUploadAssignment.as_view(), name='api_upload_assignment'),
    path('api/<str:course_code>/assignments/<int:pk>/grade/', views.ApiGradeAssignment.as_view(), name='api_grade_assignment'),
    path('api/<str:course_code>/assignments/<int:pk>/delete/', views.ApiDeleteAssignment.as_view(), name='api_delete_assignment'),
    path('api/<str:course_code>/documents/', views.ApiDocuments.as_view(), name='api_documents'),
    path('api/<str:course_code>/documents/add/', views.ApiAddDocument.as_view(), name='api_add_document'),
    path('api/<str:course_code>/documents/<int:pk>/delete/', views.ApiDeleteDocument.as_view(), name='api_delete_document'),
    path('api/<str:course_code>/forum/', views.ApiForum.as_view(), name='api_forum'),
    path('api/<str:course_code>/forum/new/', views.ApiForumNew.as_view(), name='api_forum_new'),
    path('api/<str:course_code>/forum/reply/', views.ApiForumReply.as_view(), name='api_forum_reply'),
    path('api/<str:course_code>/forum/<int:pk>/remove/', views.ApiForumRemove.as_view(), name='api_forum_remove'),
    path('api/<str:course_code>/quizzes/', views.ApiQuizzes.as_view(), name='api_quizzes'),
    path('api/<str:course_code>/quizzes/create/', views.ApiCreateQuiz.as_view(), name='api_create_quiz'),
    path('api/<str:course_code>/quizzes/<int:quiz_id>/', views.ApiQuizDetail.as_view(), name='api_quiz_detail'),
    path('api/<str:course_code>/quizzes/<int:quiz_id>/submit/', views.ApiQuizSubmit.as_view(), name='api_quiz_submit'),
    path('api/<str:course_code>/quizzes/<int:quiz_id>/remove/', views.ApiRemoveQuiz.as_view(), name='api_remove_quiz'),
    path('api/<str:course_code>/attendance/', views.ApiAttendance.as_view(), name='api_attendance'),
    path('api/<str:course_code>/attendance/roster/', views.ApiAttendanceRoster.as_view(), name='api_attendance_roster'),
    path('api/<str:course_code>/questionbank/', views.ApiQuestionBank.as_view(), name='api_questionbank'),
    path('api/<str:course_code>/questionbank/create/', views.ApiCreateBank.as_view(), name='api_create_bank'),
    path('api/<str:course_code>/questionbank/<int:bank_id>/topic/add/', views.ApiAddTopic.as_view(), name='api_add_topic'),
    path('api/<str:course_code>/questionbank/<int:bank_id>/topic/<int:topic_id>/question/add/', views.ApiAddQuestion.as_view(), name='api_add_question'),
    path('api/<str:course_code>/grading/', views.ApiGrading.as_view(), name='api_grading'),
    path('api/<str:course_code>/grading/create/', views.ApiCreateGradingScheme.as_view(), name='api_create_grading'),
    path('api/<str:course_code>/grading/evaluate/', views.ApiEvaluate.as_view(), name='api_evaluate'),
    path('api/<str:course_code>/grading/student-grades/', views.ApiStudentGrades.as_view(), name='api_student_grades'),
]
