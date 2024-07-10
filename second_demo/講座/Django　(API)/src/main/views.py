from rest_framework import generics, status
from rest_framework.response import Response
from .models import Course, Teacher, Attendance, Student
from .serializers import RegisterCourseSerializer, RegisterTeacherCourseSerializer

# 学生が講座を登録するビュー
class RegisterCourseView(generics.GenericAPIView):
    serializer_class = RegisterCourseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "講座が正常に登録されました。"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 教師が担当講座を登録するビュー
class RegisterTeacherCourseView(generics.GenericAPIView):
    serializer_class = RegisterTeacherCourseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "担当講座が正常に登録されました。"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)