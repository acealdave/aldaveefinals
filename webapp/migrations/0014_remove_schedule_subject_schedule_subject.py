# Generated by Django 4.2.7 on 2024-01-20 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_remove_schedule_subject_schedule_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='subject',
        ),
        migrations.AddField(
            model_name='schedule',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='webapp.subject'),
        ),
    ]