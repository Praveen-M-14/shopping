# Generated by Django 5.0 on 2024-10-06 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catagory',
            old_name='creted_at',
            new_name='created_at',
        ),
    ]
