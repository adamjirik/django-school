# Generated by Django 2.0.7 on 2018-07-18 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_name',
            field=models.TextField(default='name', max_length=10),
            preserve_default=False,
        ),
    ]