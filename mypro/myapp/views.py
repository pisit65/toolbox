from django.shortcuts import render

# Create your views here.
from .models import Course
from .forms import CourseSearchForm

def course_search(request):
    query = request.GET.get('query', '')  # รับค่า 'query' จาก URL
    courses = Course.objects.filter(name__icontains=query) if query else []  # ค้นหาวิชาจาก query
    return render(request, 'course_search.html', {'courses': courses, 'query': query})