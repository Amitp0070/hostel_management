# Generated by Django 5.1.1 on 2024-12-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_delete_stafflist"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="updated_at",
        ),
        migrations.AlterField(
            model_name="student",
            name="phone_number",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="student",
            name="roll_number",
            field=models.IntegerField(unique=True),
        ),
    ]