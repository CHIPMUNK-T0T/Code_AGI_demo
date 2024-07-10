from django.db import models

# 講座モデル
class Course(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=16)  # 講座ID
    teacher_id = models.BigIntegerField(db_column='TEACHER_ID', null=True, blank=True)  # 講師ID
    name = models.CharField(db_column='NAME', max_length=128)  # 講座名

    class Meta:
        db_table = 'COURSE'

# 教師モデル
class Teacher(models.Model):
    user_id = models.BigIntegerField(db_column='USER_ID', primary_key=True)  # ID
    name = models.CharField(db_column='NAME', max_length=64)  # 名前
    experience = models.IntegerField(db_column='EXPERIENCE', default=0)  # 経験

    class Meta:
        db_table = 'TEACHER'

# 受講データモデル
class Attendance(models.Model):
    course_id = models.CharField(db_column='COURSE_ID', max_length=16)  # 講座ID
    student_id = models.BigIntegerField(db_column='STUDENT_ID')  # 学生ID

    class Meta:
        db_table = 'ATTENDANCE'
        unique_together = (('course_id', 'student_id'),)  # 複合主キー

# 学生モデル
class Student(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # ID
    name = models.CharField(db_column='NAME', max_length=64)  # 名前
    course_num = models.IntegerField(db_column='COURSE_NUM', default=1)  # 受講数

    class Meta:
        db_table = 'STUDENT'