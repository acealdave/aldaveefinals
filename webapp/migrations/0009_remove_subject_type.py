# Generated by Django 4.2.7 on 2024-01-20 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_alter_subject_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='type',
        ),
    ]
