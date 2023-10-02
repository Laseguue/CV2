from django.contrib import admin
from .models import PersonalInfo, Education, Experience, Skill, PythonProject

admin.site.register(PersonalInfo)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(PythonProject)