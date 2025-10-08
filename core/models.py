from django.db import models 

class ProjectTemplate(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)  # Django, React, Next.js, etc.
    description = models.TextField()
    technologies = models.TextField(default="", blank=True)  # Added with safe default
    steps = models.TextField(default="", blank=True)  # Manual text steps
    code_snippets = models.JSONField(default=dict, blank=True)  # keep JSON for snippets if needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GeneratedProject(models.Model):
    template = models.ForeignKey(ProjectTemplate, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.namee
