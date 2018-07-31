# Generated by Django 2.0.7 on 2018-07-31 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=80)),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=15)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=25)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(default=0.01)),
                ('assignment', models.ForeignKey(db_column='assignment_id', on_delete=django.db.models.deletion.CASCADE, to='school.Assignment')),
                ('student', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='assignments',
            field=models.ManyToManyField(through='school.StudentAssignment', to='school.Assignment'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(to='school.Student'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Group'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='students',
            field=models.ManyToManyField(through='school.StudentAssignment', to='school.Student'),
        ),
    ]
