from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('experience/<int:experience_id>/', views.experience_detail, name='experience_detail'),
    path('skills/', views.skills, name='skills'),
    path('skills/<int:skill_id>/', views.skill_detail, name='skill_detail'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('python_projects/', views.python_projects, name='python_projects'),
]