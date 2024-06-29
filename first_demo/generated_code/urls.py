from django.urls import path
from .views import LoginView, RegisterView, ProjectListView, ProjectDetailView, TaskDetailView

urlpatterns = [
    # ログイン画面のURLパターン
    path('login/', LoginView.as_view(), name='login'),
    
    # 新規登録画面のURLパターン
    path('register/', RegisterView.as_view(), name='register'),
    
    # プロジェクト一覧画面のURLパターン
    path('projects/', ProjectListView.as_view(), name='project_list'),
    
    # プロジェクト詳細画面のURLパターン
    path('projects/<int:project_id>/', ProjectDetailView.as_view(), name='project_detail'),
    
    # タスク詳細画面のURLパターン
    path('tasks/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
]