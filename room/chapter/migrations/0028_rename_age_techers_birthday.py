# Generated by Django 5.0.6 on 2024-09-10 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0027_alter_techers_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='techers',
            old_name='age',
            new_name='birthday',
        ),
    ]