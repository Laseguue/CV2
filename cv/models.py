from django.db import models
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

class PersonalInfo(models.Model):
    photo = models.ImageField(upload_to='photos/', max_length=500)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(max_length=255)
    github = models.URLField(max_length=255)
    summary = models.TextField(blank=True)

class Education(models.Model):
    diploma = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.IntegerField()
    image = models.ImageField(upload_to='education_images/', max_length=500)
    is_ongoing = models.BooleanField(default=False)

class Experience(models.Model):
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    tasks = models.TextField()
    diplome_image = models.ImageField(upload_to='diplomes/', null=True, blank=True, max_length=500)

class Skill(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    certificate_image = models.ImageField(upload_to='skill_images/', max_length=500)

class PythonProject(models.Model):
    title = models.CharField(max_length=255)
    github_link = models.URLField(max_length=255)
    description = models.TextField(blank=True)
    readme_image = models.ImageField(upload_to='project_images/', null=True, blank=True, max_length=500)