from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Project, Task

# ログイン画面のビュー
class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_name = request.POST.get('USER_NAME')
        password = request.POST.get('PASSWORD')

        if not user_name or not password:
            messages.error(request, 'ユーザー名またはパスワードが入力されていません')
            return render(request, self.template_name)

        if len(password) < 6:
            messages.error(request, 'パスワードが短すぎます')
            return render(request, self.template_name)

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('project_list')
        else:
            messages.error(request, 'ユーザー情報が正しくありません')
            return render(request, self.template_name)

# 新規登録画面のビュー
class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_name = request.POST.get('USER_NAME')
        password = request.POST.get('PASSWORD')

        if not user_name or not password:
            messages.error(request, 'ユーザー名またはパスワードが入力されていません')
            return render(request, self.template_name)

        if len(password) < 6:
            messages.error(request, 'パスワードが短すぎます')
            return render(request, self.template_name)

        if User.objects.filter(username=user_name).exists():
            messages.error(request, 'ユーザーは既に登録されています')
            return render(request, self.template_name)

        user = User.objects.create_user(username=user_name, password=password)
        user.save()
        messages.success(request, 'ユーザー登録が完了しました')
        return redirect('login')

# プロジェクト一覧画面のビュー
class ProjectListView(View):
    template_name = 'project_list.html'

    def get(self, request):
        user = request.user
        projects = Project.objects.filter(project_user__user_id=user.id).order_by('project_id')
        project_data = []

        for project in projects:
            project_members = project.project_user_set.count()
            remaining_tasks = project.task_set.exclude(status='完了済み').count()
            project_data.append({
                'project_id': project.project_id,
                'project_name': project.project_name,
                'project_members': project_members,
                'remaining_tasks': remaining_tasks
            })

        return render(request, self.template_name, {'projects': project_data})

# プロジェクト詳細画面のビュー
class ProjectDetailView(View):
    template_name = 'project_detail.html'

    def get(self, request, project_id):
        project = get_object_or_404(Project, pk=project_id)
        tasks = project.task_set.order_by('task_id')
        return render(request, self.template_name, {'project': project, 'tasks': tasks})

# タスク詳細画面のビュー
class TaskDetailView(View):
    template_name = 'task_detail.html'

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        return render(request, self.template_name, {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        task.task_name = request.POST.get('TASK_NAME', task.task_name)
        task.contents = request.POST.get('TASK_DESCRIPTION', task.contents)
        task.assign_id = request.POST.get('ASSIGN', task.assign_id)
        task.status = request.POST.get('STATUS', task.status)
        task.start_day = request.POST.get('START_DAY', task.start_day)
        task.end_day = request.POST.get('END_DAY', task.end_day)
        task.save()
        messages.success(request, 'タスクが更新されました')
        return redirect('task_detail', task_id=task_id)