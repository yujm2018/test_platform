# Generated by Django 2.1.7 on 2019-03-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=True, verbose_name='状态'),
        ),
    ]
