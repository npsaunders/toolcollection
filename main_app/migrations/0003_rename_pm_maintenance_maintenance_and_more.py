# Generated by Django 4.1.2 on 2022-10-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_maintenance"),
    ]

    operations = [
        migrations.RenameField(
            model_name="maintenance",
            old_name="pm",
            new_name="maintenance",
        ),
        migrations.AlterField(
            model_name="maintenance",
            name="date",
            field=models.DateField(verbose_name="maintenance date"),
        ),
    ]