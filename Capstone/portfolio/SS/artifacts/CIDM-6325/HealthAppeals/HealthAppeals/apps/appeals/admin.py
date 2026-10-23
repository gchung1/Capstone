from django.contrib import admin
from .models import Template

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

    # Better feature - admin fieldsets
    fieldsets = (
        ("Template Information", {
            "fields": ("name",)
        }),
        ("Template Content", {
            "fields": ("text",),
            "description": "Edit the default text that will be used when generating appeal letters.",
        }),
    )
