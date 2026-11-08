from django.urls import path
from . import views

app_name = "appeals"

urlpatterns = [
    path("", views.generate_letter, name="generate_letter"),
    path("download-pdf/", views.download_pdf, name="download_pdf"),
    path("template/<int:id>/", views.template_detail, name="template_detail"),
    path("templates/", views.template_list, name="template_list"),


    # New CBVs - HomeView and TemplatePreviewView
    path("home/", views.HomeView.as_view(), name="home"),
    path("template-preview/", views.TemplatePreviewView.as_view(), name="template_preview"),


    # Admin CRUD for Templates
    path("admin/templates/", views.admin_template_list, name="admin_template_list"),
    path("admin/templates/create/", views.admin_template_create, name="admin_template_create"),
    path("admin/templates/<int:pk>/edit/", views.admin_template_update, name="admin_template_update"),
    path("admin/templates/<int:pk>/delete/", views.admin_template_delete, name="admin_template_delete"),


]
