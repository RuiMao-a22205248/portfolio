from django.shortcuts import render
import datetime


# Create your views here.
def home_view(request):
    return render(request, 'portfolio/home.html')


def me_view(request):
    return render(request, 'portfolio/me.html')


def project_view(request):
    return render(request, 'portfolio/project.html')


def pw_view(request):
    return render(request, 'portfolio/pw.html')


def blog_view(request):
    return render(request, 'portfolio/blog.html')


def site_view(request):
    return render(request, 'portfolio/site.html')


def tool_view(request):
    return render(request, 'portfolio/tool.html')
