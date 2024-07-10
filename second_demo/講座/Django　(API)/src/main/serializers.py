from rest_framework import serializers
from .models import Course, Teacher

# 教師が担当講座を登録するためのシリアライザ
class RegisterTeacherCourseSerializer(serializers.Serializer):
    teacher_id = serializers.IntegerField()
    course_id = serializers.CharField(max_length=16)
    experience = serializers.IntegerField(required=False)

    def validate_teacher_id(self, value):
        if not Teacher.objects.filter(user_id=value).exists():
            raise serializers.ValidationError("教師が存在しません。")
        return value

    def validate_course_id(self, value):
        if not Course.objects.filter(id=value).exists():
            raise serializers.ValidationError("講座が存在しません。")
        return value

    def create(self, validated_data):
        teacher_id = validated_data['teacher_id']
        course_id = validated_data['course_id']
        experience = validated_data.get('experience', 0)

        course = Course.objects.get(id=course_id)
        course.teacher_id = teacher_id
        course.save()

        if experience:
            teacher = Teacher.objects.get(user_id=teacher_id)
            teacher.experience += experience
            teacher.save()

        return validated_data