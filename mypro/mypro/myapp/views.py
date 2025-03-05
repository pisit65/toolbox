from django.db import models

# โมเดลสำหรับเก็บข้อมูลรายวิชา
class Course(models.Model):
    name = models.CharField(max_length=200)  # ชื่อวิชา
    description = models.TextField(blank=True)  # รายละเอียดวิชา (optional)

    def __str__(self):
        return self.name
