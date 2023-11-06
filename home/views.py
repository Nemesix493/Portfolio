from django.shortcuts import render

from .models import HomePageDescription
from project.models import Project

# Create your views here.

def home_page(request):
    description = HomePageDescription.objects.get(pk=0)
    projects = Project.objects.all()
    return render(
        request,
        'home/home_page.html',
        {
            'page_title': 'Home Page',
            'projects': projects,
            'description': description
        }
    )
