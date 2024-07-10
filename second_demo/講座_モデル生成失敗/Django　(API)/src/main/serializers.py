from rest_framework import serializers

# 教師が担当講座を登録するためのシリアライザ
class AssignTeacherSerializer(serializers.Serializer):
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