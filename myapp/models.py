from django.db import models

# Create your models here.
class Course(models.Model):
    code = models.CharField(max_length=10 , unique=True) #รหัสวิชา
    name = models.CharField(max_length=255) #ชื่อวิชา
    description = models.TextField() #รายละเอียดวิชา

    def __str__ (self):
        return self.code + " " + self.name