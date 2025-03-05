# urls.py
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.course_search, name='course_search'),  # เพิ่ม search/ ให้ตรงกับที่คุณต้องการ
]
