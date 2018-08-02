# Generated by Django 2.0.7 on 2018-08-01 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20180801_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_of_week', models.CharField(
                    choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'),
                             ('6', 'Saturday'), ('7', 'Sunday')], max_length=1)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Classroom')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Group')),
            ],
            options={
                'verbose_name': 'Lessons',
                'verbose_name_plural': 'Lessons',
                'ordering': ['days_of_week', 'start_time'],
            },
        ),
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.Teacher'),
        )
    ]
