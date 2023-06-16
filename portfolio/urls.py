from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('home/', views.home_view, name="home"),
    path('me/', views.me_view, name="me"),
    path('project/', views.project_view, name="project"),
    path('pw/', views.pw_view, name="pw"),
    path('blog/', views.blog_view, name="blog"),
    path('site/', views.me_view, name="site"),
    path('tool/', views.tool_view, name="tool"),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]
