from django.contrib import admin
from django.urls import path, include
from apps.appeals.views import generate_letter


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", generate_letter),
    path("appeals/", include("apps.appeals.urls")), 
    path("auth/", include("django.contrib.auth.urls")),

]
