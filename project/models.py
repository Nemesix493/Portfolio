from django.db import models

# Create your models here.

class Techno(models.Model):
    name = models.CharField(
        max_length=60,
        null=False,
        blank=False,
        unique=True
    )
    description = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )
    website = models.URLField(
        null=False,
        blank=False
    )
    BEGINNER = "BG"
    INTERMEDIATE = "IT"
    CONFIRMED = "CF"
    EXPERT = "EX"
    LEVELS = [
        (BEGINNER, "Beginner"),
        (INTERMEDIATE, 'Intermediate'),
        (CONFIRMED, 'Confirmed'),
        (EXPERT, 'Expert')
    ]
    level = models.CharField(
        max_length=2,
        choices=LEVELS,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=60,
        null=False,
        blank=False,
        unique=True
    )
    description = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )
    last_push = models.DateTimeField(
        null=False,
        blank=False
    )
    add_date = models.DateTimeField(
        auto_now_add=True
    )
    technologies = models.ManyToManyField(
        to=Techno,
        related_name='projects',
        blank=True
    )

    def __str__(self):
        return self.name


class ProjectLink(models.Model):
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='links',

    )
    name=models.CharField(
        max_length=60,
        null=False,
        blank=False
    )
    url = models.URLField(
        null=False,
        blank=False
    )

    @property
    def project_name(self):
        return self.project.name
    
    def __str__(self):
        return f'{self.project_name} {self.name}'
