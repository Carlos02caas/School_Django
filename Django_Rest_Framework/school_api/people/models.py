from django.db import models
from codes.models import PersonType, Gender, Nationality, MaritalStatus, State
from school.models import School
    
class People(models.Model):
    people_id = models.CharField(max_length=5, unique=True, editable=False)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    person_type = models.ForeignKey(PersonType,to_field='code_value', on_delete=models.PROTECT)
    date_of_birth = models.DateField()
    ssn = models.CharField(max_length=11, blank=True, null=True)
    gender = models.ForeignKey(Gender, to_field='code_value', on_delete=models.PROTECT)
    nationality = models.ForeignKey(Nationality, to_field='code_value', on_delete=models.PROTECT)
    marital_status = models.ForeignKey(MaritalStatus, to_field='code_value', on_delete=models.PROTECT)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.ForeignKey(State, to_field='code_value', on_delete=models.PROTECT)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    phone = models.CharField(max_length=15)
    phone_code = models.CharField(max_length=4)
    email = models.EmailField()
    school = models.ForeignKey(School, on_delete=models.PROTECT)
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.people_id:
            self.people_id = str(self.id).zfill(5)
            super().save(update_fields=['people_id'])

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Matricula: {self.people_id}"
