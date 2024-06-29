from django.contrib import admin
from .models import User, Project, Task

# ユーザーモデルの管理クラス
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name',)

# プロジェクトモデルの管理クラス
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name',)

# タスクモデルの管理クラス
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'status')

# 管理サイトへのモデルの登録
admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)