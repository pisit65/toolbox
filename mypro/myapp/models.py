from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)  # ชื่อวิชา

    def __str__(self):
        return self.name