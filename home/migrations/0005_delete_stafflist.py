# Generated by Django 5.1.1 on 2024-12-09 13:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_rename_position_stafflist_designation_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Stafflist",
        ),
    ]