# Generated by Django 4.2.4 on 2023-08-27 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0005_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='email',
            new_name='doc_email',
        ),
    ]
