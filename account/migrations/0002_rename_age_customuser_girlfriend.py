# Generated by Django 5.0.2 on 2024-04-11 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='age',
            new_name='girlfriend',
        ),
    ]
