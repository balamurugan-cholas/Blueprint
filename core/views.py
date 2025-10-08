from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import ProjectTemplate, GeneratedProject
from django.db import models

# --- Dashboard ---
def dashboard(request):
    all_projects = GeneratedProject.objects.all().order_by('-created_at')
    recent_projects = all_projects[:3]

    context = {
        "recent_projects": recent_projects,
        "all_projects": all_projects
    }
    return render(request, "home.html", context)


# --- Generate Page ---
def generate(request):
    template_id = request.GET.get("template_id")
    selected_template = None

    # If opened from search suggestion → load that template
    if template_id:
        try:
            selected_template = ProjectTemplate.objects.get(id=template_id)
        except ProjectTemplate.DoesNotExist:
            selected_template = None

    # Organize all templates by category (same as before)
    templates = ProjectTemplate.objects.all().order_by("category", "name")
    categories = {}
    for template in templates:
        categories.setdefault(template.category, []).append(template)

    return render(request, "generate.html", {
        "categories": categories,
        "selected_template": selected_template
    })


# --- Generate Project ---
@csrf_exempt
def generate_project(request):
    if request.method == "POST":
        template_id = request.POST.get("template_id")
        if not template_id:
            return JsonResponse({"success": False, "error": "No template ID provided."})

        try:
            template = ProjectTemplate.objects.get(id=template_id)
        except ProjectTemplate.DoesNotExist:
            return JsonResponse({"success": False, "error": "Template not found."})

        project = GeneratedProject.objects.create(
            template=template,
            name=template.name
        )

        return JsonResponse({
            "success": True,
            "project_id": project.id,
            "project_name": project.name,
            "created_at": project.created_at.strftime("%Y-%m-%d %H:%M:%S")
        })

    return JsonResponse({"success": False, "error": "Invalid request method."})


# --- Delete Project ---
@csrf_exempt
def delete_project(request):
    if request.method == "POST":
        project_id = request.POST.get("project_id")
        if not project_id:
            return JsonResponse({"success": False, "error": "Project ID missing."})
        try:
            project = GeneratedProject.objects.get(id=project_id)
            project.delete()
            return JsonResponse({"success": True})
        except GeneratedProject.DoesNotExist:
            return JsonResponse({"success": False, "error": "Project not found."})
    return JsonResponse({"success": False, "error": "Invalid request method."})


# --- Open Project ---
def open_project(request, project_id):
    try:
        project = GeneratedProject.objects.get(id=project_id)
        data = {
            "success": True,
            "project_name": project.name,
            "created_at": project.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "template_name": project.template.name,
            "description": project.template.description,
            "technologies": project.template.technologies,
            "steps": project.template.steps,
        }
        return JsonResponse(data)
    except GeneratedProject.DoesNotExist:
        return JsonResponse({"success": False, "error": "Project not found."})


# --- Live Search ---
def search_projects(request):
    query = request.GET.get("q", "").strip()
    results = []

    if query:
        projects = ProjectTemplate.objects.filter(
            models.Q(name__icontains=query) | models.Q(category__icontains=query)
        ).order_by("name")[:10]  # limit to 10 results

        results = [
            {
                "id": p.id,
                "name": p.name,
                "category": p.category,
                "description": p.description[:80] + ("..." if len(p.description) > 80 else "")
            }
            for p in projects
        ]

    return JsonResponse({"results": results})

def history(request):
    # Get all generated projects ordered by latest first
    projects = GeneratedProject.objects.all().order_by('-created_at')
    context = {"projects": projects}
    return render(request, "history.html", context)
