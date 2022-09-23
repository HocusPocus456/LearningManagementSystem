# Generated by Django 4.1.1 on 2022-09-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_featured_img_course_techs'),
    ]

    operations = [
        migrations.AddField(
            model_name='learner',
            name='otp_digit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='learner',
            name='verify_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tutor',
            name='otp_digit',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tutor',
            name='verify_status',
            field=models.BooleanField(default=False),
        ),
    ]
