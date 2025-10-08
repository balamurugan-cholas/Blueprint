from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),       # home/dashboard page
    path('generator/', include('generator.urls')),  # generator app routes
]
