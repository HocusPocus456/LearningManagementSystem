# Generated by Django 4.1.1 on 2022-10-15 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_courserating_course_alter_courserating_learner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courserating',
            options={'verbose_name_plural': '8. Learner Favourite Courses'},
        ),
        migrations.AlterField(
            model_name='courserating',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course'),
        ),
        migrations.AlterField(
            model_name='courserating',
            name='learner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.learner'),
        ),
        migrations.CreateModel(
            name='LearnerFavouriteCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('learner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.learner')),
            ],
            options={
                'verbose_name_plural': '7. Learner Favourite Courses',
            },
        ),
    ]