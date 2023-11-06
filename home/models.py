from django.db import models

# Create your models here.

class HomePageDescription(models.Model):
    title = models.CharField(
        max_length=40,
        blank=False,
        null=True
    )
    second_title = models.CharField(
        max_length=60,
        blank=False,
        null=True
    )
    description = models.TextField(
        max_length=500,
        blank=False,
        null=True
    )

    def __str__(self) -> str:
        return 'Section de descripiton de la page d\'acceuil'
