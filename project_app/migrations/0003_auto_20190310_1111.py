# Generated by Django 2.1.7 on 2019-03-10 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_auto_20190303_0000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': '模块管理', 'verbose_name_plural': '模块管理'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '项目管理', 'verbose_name_plural': '项目管理'},
        ),
    ]