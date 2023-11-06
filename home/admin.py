from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from .models import HomePageDescription


@admin.register(HomePageDescription)
class HomePageDescriptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'second_title']

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj: Any = None) -> bool:
        return False
