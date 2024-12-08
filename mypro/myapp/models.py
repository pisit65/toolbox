from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)  # ชื่อรายวิชา
    code = models.CharField(max_length=10) 

    def __str__(self):
        return self.name