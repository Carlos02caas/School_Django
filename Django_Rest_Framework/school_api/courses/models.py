from django.db import models
from people.models import People

class AcademicPeriod(models.Model):
    code_value = models.CharField(max_length=6, unique=True)
    year = models.IntegerField()
    term = models.CharField(max_length=8)
    name = models.CharField(max_length=15)

    start_date = models.DateField()
    end_date = models.DateField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code_value} - {self.name}"

class Course(models.Model):
    name = models.CharField(max_length=30)
    course_code = models.CharField(max_length=15, unique=True)
    area = models.CharField(max_length=15
                            )
    description = models.TextField()
    credits = models.IntegerField()
    is_active = models.BooleanField(default=True)
    max_enrollments = models.IntegerField(default=0)
    min_enrollments = models.IntegerField(default=0)
    current_enrollments = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.course_code} - {self.name}"
    
class CoursePeriod(models.Model):
    course = models.ForeignKey(Course,to_field='course_code', on_delete=models.PROTECT)
    period = models.ForeignKey(AcademicPeriod, to_field='code_value', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    max_enrollments = models.IntegerField(default=0)
    min_enrollments = models.IntegerField(default=0)
    current_enrollments = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.course.course_code} - {self.classroom}"

    
class CourseSchedule(models.Model):
    course_period = models.ForeignKey(CoursePeriod, on_delete=models.PROTECT)
    classroom = models.CharField(max_length=15)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.course_code} - {self.classroom} - {self.day} - {self.start_time} - {self.end_time}"
    
class Enrollment(models.Model):
    student = models.ForeignKey(People, on_delete=models.PROTECT)
    course_period = models.ForeignKey(CoursePeriod, on_delete=models.PROTECT)
    schedules = models.ManyToManyField(CourseSchedule)

    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.course_period.period.code_value}"