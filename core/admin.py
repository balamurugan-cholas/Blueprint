from django.contrib import admin
from .models import ProjectTemplate, GeneratedProject

admin.site.register(ProjectTemplate)
admin.site.register(GeneratedProject)

