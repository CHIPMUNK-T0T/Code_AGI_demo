from rest_framework import generics, status
from rest_framework.response import Response
from .models import Course, Teacher, Student
from .serializers import CourseSerializer, TeacherSerializer, StudentSerializer, RegisterCourseSerializer, AssignTeacherSerializer

# 学生が講座を登録するビュー
class RegisterCourseView(generics.GenericAPIView):
    serializer_class = RegisterCourseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            student_id = serializer.validated_data['student_id']
            course_id = serializer.validated_data['course_id']

            # 学生が存在するか確認
            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return Response({"error": "学生が存在しません。"}, status=status.HTTP_400_BAD_REQUEST)

            # 学生_講座の対応を確認
            if not student.course_set.filter(id=course_id).exists():
                course = Course.objects.get(id=course_id)
                student.course_set.add(course)
                student.course_num += 1
                student.save()

            return Response({"message": "講座が正常に登録されました。"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 教師が担当講座を登録するビュー
class AssignTeacherView(generics.GenericAPIView):
    serializer_class = AssignTeacherSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            teacher_id = serializer.validated_data['teacher_id']
            course_id = serializer.validated_data['course_id']
            experience = serializer.validated_data.get('experience', None)

            # 教師が存在するか確認
            try:
                teacher = Teacher.objects.get(user_id=teacher_id)
            except Teacher.DoesNotExist:
                return Response({"error": "教師が存在しません。"}, status=status.HTTP_400_BAD_REQUEST)

            # 講座に教師を紐づけ
            course = Course.objects.get(id=course_id)
            course.teacher_id = teacher_id
            course.save()

            # 経験年数が入力されていれば更新
            if experience is not None:
                teacher.experience += 1
                teacher.save()

            return Response({"message": "講座が正常に担当されました。"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)