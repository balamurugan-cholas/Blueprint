# generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate, name='home'),  # if dashboard is here
    path('generate/', views.generate, name='generate'),
    path('generate-project/', views.generate_project, name='generate_project'),
    path('delete-project/', views.delete_project, name='delete_project'),
    path('open-project/<int:project_id>/', views.open_project, name='open_project'),
]
