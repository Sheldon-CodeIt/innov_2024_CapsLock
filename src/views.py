from django.shortcuts import render
from course.models import Course

def main_home(request):
    courses = Course.objects.all()
    # return render(request, 'accounts/index.html', {'user_profile': user_profile})
    return render(request, 'accounts/index.html', {"courses": courses})
