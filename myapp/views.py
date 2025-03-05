from django.shortcuts import render
from .models import Course

# Create your views here.

def search_by_name(request):
    query = request.GET.get('query', '')  # ดึงค่าจาก query, ถ้าไม่มีจะได้ค่าว่าง
    courses = Course.objects.filter(name__icontains=query)  # ค้นหาตามชื่อวิชา
    return render(request, 'search.html', {'courses': courses, 'query': query})
