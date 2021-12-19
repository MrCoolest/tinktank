from django.db import models
from django.db.models.fields import CharField


# Create your models here.
class Students(models.Model):
     student_name = models.CharField(max_length=50)
     college_name = models.CharField(max_length=200)
     Specialisation = models.CharField(max_length=100)
     Degree_name = models.CharField(max_length=100)
     Internship = models.CharField(max_length=100)
     Phone_no = models.CharField(max_length=20)
     Email = models.CharField(max_length=100)
     Location = models.CharField(max_length=200)
     Gender = models.CharField(max_length=50)
     note = models.TextField(max_length=500, default='')

     def __str__(self) -> str:
         return self.student_name

status = (
     ('Inactive','Inactive'),
     ('Active','Active')
)


class User(models.Model):
     user_name = models.CharField(max_length=100)
     password = models.CharField(max_length=100)
     user_status = models.CharField(max_length=20, choices=status, default='Inactive')

     def __str__(self) -> str:
          return self.user_name


