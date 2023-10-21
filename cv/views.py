from django.shortcuts import render, get_object_or_404, redirect
from .models import PersonalInfo, Education, Experience, Skill, PythonProject
from django.core.mail import send_mail
from .forms import ContactForm


def home(request):
    personal_info = PersonalInfo.objects.first()
    return render(request, 'cv/home.html', {'personal_info': personal_info})


def about(request):
    personal_info = PersonalInfo.objects.first()
    return render(request, 'cv/about.html', {'personal_info': personal_info})


def experience(request):
    experiences = Experience.objects.all()
    personal_info = PersonalInfo.objects.first()
    return render(request, 'cv/experience.html', {'experiences': experiences, 'personal_info': personal_info})


def experience_detail(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)
    personal_info = PersonalInfo.objects.first()
    return render(request, 'cv/experience_detail.html', {'experience': experience, 'personal_info': personal_info})


def skills(request):
    skills = Skill.objects.all()
    personal_info = PersonalInfo.objects.first()
    return render(request, 'cv/skills.html', {'skills': skills, 'personal_info': personal_info})


def skill_detail(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    personal_info = PersonalInfo.objects.first()
    return render(request, 'cv/skill_detail.html', {'skill': skill, 'personal_info': personal_info})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            email_body = f"Nom: {name}\nEmail: {email}\nTéléphone: {phone}\n\nMessage:\n{message}"

            send_mail(
                f'Contact de {name}',
                email_body,
                email,
                ['ghostdogthe1@gmail.com'],
            )

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'cv/contact.html', {'form': form})

def success(request):
    return render(request, 'cv/success.html')

def python_projects(request):
    projects = PythonProject.objects.all()
    personal_info = PersonalInfo.objects.first()
    return render(request, 'cv/python_projects.html', {'projects': projects, 'personal_info': personal_info})