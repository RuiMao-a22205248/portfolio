from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect('portfolio:blog')
        else:
            return render(request, 'portfolio/login.html', {
                'message': 'Credenciais invalidas'
            })
    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return redirect('portfolio:blog')

