from rest_framework import serializers
from .models import Course, CourseSchedule, AcademicPeriod, CoursePeriod, Enrollment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AcademicPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicPeriod
        fields = '__all__'

class CourseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSchedule
        fields = '__all__'

    def validate(self, data):
        course = data.get('course')
        period = data.get('period')
        day = data.get('day')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time > end_time:
            raise serializers.ValidationError("Start time must be before end time.")
        
        queryset = CourseSchedule.objects.filter(
            course=course,
            period=period,
            day__iexact=day,
        )

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        conflict = queryset.filter(
            start_time__lt=end_time,
            end_time__gt=start_time
        )

        if conflict.exists():
            raise serializers.ValidationError("A classroom with this time range already exists.")
        
        return data
    
class CoursePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePeriod
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'