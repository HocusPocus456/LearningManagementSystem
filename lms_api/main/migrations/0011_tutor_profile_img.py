# Generated by Django 4.1.1 on 2022-10-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_tutor_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='tutor_profile_imgs/'),
        ),
    ]