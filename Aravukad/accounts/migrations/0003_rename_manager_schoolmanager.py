# Generated by Django 4.0.4 on 2022-05-16 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_institution_institution'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manager',
            new_name='SchoolManager',
        ),
    ]
