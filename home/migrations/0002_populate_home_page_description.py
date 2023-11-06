from django.db import migrations, models

def add_home_page_description(apps, schema_editor):
    home_page_description_model = apps.get_model("home", "HomePageDescription")
    home_page_description_model.objects.create(
        title='Kevin Verquerre',
        id=0
    )

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial')
    ]

    operations = [
        migrations.RunPython(add_home_page_description),
    ]