from django.shortcuts import render

from project.models import Project

# Create your views here.

def home_page(request):
    projects = Project.objects.all()
    return render(
        request,
        'home/home_page.html',
        {
            'page_title': 'Home Page',
            'projects': projects
        }
    )