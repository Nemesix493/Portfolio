from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home/home_page.html', {'page_title': 'Home Page'})