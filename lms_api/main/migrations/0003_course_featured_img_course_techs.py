# Generated by Django 4.1.1 on 2022-09-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_address_tutor_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='featured_img',
            field=models.ImageField(null=True, upload_to='course_imgs/'),
        ),
        migrations.AddField(
            model_name='course',
            name='techs',
            field=models.TextField(null=True),
        ),
    ]