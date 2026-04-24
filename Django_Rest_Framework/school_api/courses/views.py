from django.shortcuts import render
from rest_framework import viewsets
from .models import Course, CourseSchedule, AcademicPeriod, CoursePeriod, Enrollment
from .serializers import CourseSerializer, CourseScheduleSerializer, AcademicPeriodSerializer, CoursePeriodSerializer, EnrollmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseScheduleViewSet(viewsets.ModelViewSet):
    queryset = CourseSchedule.objects.all()
    serializer_class = CourseScheduleSerializer

class AcademicPeriodViewSet(viewsets.ModelViewSet):
    queryset = AcademicPeriod.objects.all()
    serializer_class = AcademicPeriodSerializer

class CoursePeriodViewSet(viewsets.ModelViewSet):
    queryset = CoursePeriod.objects.all()
    serializer_class = CoursePeriodSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer