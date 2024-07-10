from django.urls import path
from .views import RegisterCourseView, RegisterTeacherCourseView

# URLパターンの定義
urlpatterns = [
    path('register_course/', RegisterCourseView.as_view(), name='register_course'),
    path('register_teacher_course/', RegisterTeacherCourseView.as_view(), name='register_teacher_course'),
]