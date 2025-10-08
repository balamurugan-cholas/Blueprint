from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.models import ProjectTemplate, GeneratedProject

# --- Generate Templates Page ---
def generate(request):
    # Fetch all templates, ordered by category then name
    templates = ProjectTemplate.objects.all().order_by("category", "name")

    # Group templates by category
    categories = {}
    for template in templates:
        categories.setdefault(template.category, []).append(template)

    return render(request, "generate.html", {"categories": categories})


# --- Generate Project (from template) ---
def generate_project(request):
    if request.method == "POST":
        template_id = request.POST.get("template_id")
        if not template_id:
            return JsonResponse({"success": False, "error": "No template ID provided."})

        try:
            template = ProjectTemplate.objects.get(id=template_id)
        except ProjectTemplate.DoesNotExist:
            return JsonResponse({"success": False, "error": "Template not found."})

        # Create a new GeneratedProject
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


# --- Open Project (to show details in modal) ---
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
