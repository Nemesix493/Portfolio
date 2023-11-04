from django.template import Library

register = Library()

@register.filter
def project_thumbnail_title(title: str) -> str:
    return '_' + title.replace(' ', '_')