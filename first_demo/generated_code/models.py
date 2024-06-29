from django.db import models

# ユーザーモデル
class User(models.Model):
    user_id = models.AutoField(primary_key=True, db_column='USER_ID')
    user_name = models.CharField(max_length=32, db_column='USER_NAME')
    password = models.CharField(max_length=32, db_column='PASSWORD')

    class Meta:
        db_table = 'ユーザー'

# プロジェクトモデル
class Project(models.Model):
    project_id = models.AutoField(primary_key=True, db_column='PROJECT_ID')
    project_name = models.CharField(max_length=50, db_column='PROJECT_NAME')
    purpose = models.CharField(max_length=300, db_column='PURPOSE', blank=True, null=True)

    class Meta:
        db_table = 'プロジェクト'

# タスクモデル
class Task(models.Model):
    task_id = models.AutoField(primary_key=True, db_column='TASK_ID')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, db_column='PROJECT_ID')
    task_name = models.CharField(max_length=50, db_column='TASK_NAME')
    contents = models.CharField(max_length=1000, db_column='CONTENTS', default='タスク内容')
    register = models.ForeignKey(User, related_name='registered_tasks', on_delete=models.CASCADE, db_column='REGISTER_ID')
    assign = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.SET_NULL, null=True, blank=True, db_column='ASSIGN_ID')
    status = models.CharField(max_length=10, db_column='STATUS', default='未開始', choices=[('未開始', '未開始'), ('実行中', '実行中'), ('完了済み', '完了済み'), ('保留中', '保留中')])
    start_day = models.DateField(db_column='START_DAY', blank=True, null=True)
    end_day = models.DateField(db_column='END_DAY', blank=True, null=True)

    class Meta:
        db_table = 'タスク'