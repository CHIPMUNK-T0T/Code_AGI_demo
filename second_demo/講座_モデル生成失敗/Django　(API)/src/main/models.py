from django.db import models

# 講座モデル
class Course(models.Model):
    # 講座ID
    id = models.CharField(db_column='ID', primary_key=True, max_length=16)
    # 講師ID
    teacher_id = models.BigIntegerField(db_column='TEACHER_ID', null=True, blank=True)
    # 講座名
    name = models.CharField(db_column='NAME', max_length=128)

    class Meta:
        db_table = '講座'

# 教師モデル
class Teacher(models.Model):
    # ID
    user_id = models.BigIntegerField(db_column='USER_ID', primary_key=True)
    # 名前
    name = models.CharField(db_column='NAME', max_length=64)
    # 経験
    experience = models.IntegerField(db_column='EXPERIENCE', default=0)

    class Meta:
        db_table = '教師'

# 学生モデル
class Student(models.Model):
    # ID
    id = models.BigIntegerField(db_column='ID', primary_key=True)
    # 名前
    name = models.CharField(db_column='NAME', max_length=64)
    # 受講数
    course_num = models.IntegerField(db_column='COURCE_NUM', default=1)

    class Meta:
        db_table = '学生'