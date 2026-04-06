from django.db import models


class PersonType(models.Model):
    code_value = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=15)
    long_name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.code_value} - {self.name}"
    
class Gender(models.Model):
    code_value = models.CharField(max_length=1, unique=True)
    name = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.code_value} - {self.name}"

class MaritalStatus(models.Model):
    code_value = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.code_value} - {self.name}"
    
class Nationality(models.Model):
    code_value = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=15)
    long_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.code_value} - {self.name}"
    
class State(models.Model):
    code_value = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=15)
    long_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.code_value} - {self.name}"