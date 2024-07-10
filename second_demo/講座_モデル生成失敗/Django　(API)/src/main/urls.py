from django.urls import path
from .views import RegisterCourseView, AssignTeacherView

urlpatterns = [
    # 学生が講座を登録するエンドポイント
    path('register_course/', RegisterCourseView.as_view(), name='register_course'),
    
    # 教師が担当講座を登録するエンドポイント
    path('assign_teacher/', AssignTeacherView.as_view(), name='assign_teacher'),
]