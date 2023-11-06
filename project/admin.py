from django.contrib import admin

from .models import ProjectLink, Project, Techno


@admin.register(Techno)
class TechnoAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_push']


@admin.register(ProjectLink)
class ProjectLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'project_name']
