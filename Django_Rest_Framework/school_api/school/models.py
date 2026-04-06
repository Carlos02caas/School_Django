from django.db import models
from codes.models import State

class School(models.Model):
    school_id = models.CharField(max_length=3, unique=True, editable=False)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.ForeignKey(State, to_field='code_value', on_delete=models.PROTECT)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    phone_code = models.CharField(max_length=4)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.school_id:
            self.school_id = str(self.id).zfill(3)
            super().save(update_fields=['school_id'])