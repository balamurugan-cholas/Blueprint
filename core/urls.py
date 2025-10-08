from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path('generate/', views.generate, name='generate'),
    path('generate-project/', views.generate_project, name='generate_project'),  # <- add this
    path('delete-project/', views.delete_project, name='delete_project'),
    path('open-project/<int:project_id>/', views.open_project, name='open_project'),
    path("search/", views.search_projects, name="search_projects"),
    path('history/', views.history, name='history'),
]
