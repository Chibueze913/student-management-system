from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20,unique=True)
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    course = models.CharField(max_length=20)
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"