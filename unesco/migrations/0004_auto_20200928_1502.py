# Generated by Django 3.0.8 on 2020-09-28 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0003_auto_20200928_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iso',
            old_name='iso',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='region',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='states',
            old_name='states',
            new_name='name',
        ),
    ]