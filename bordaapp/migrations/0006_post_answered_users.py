# Generated by Django 3.2.9 on 2021-12-01 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bordaapp', '0005_submission_submitted_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='answered_users',
            field=models.TextField(default=''),
        ),
    ]
