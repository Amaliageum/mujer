# Generated by Django 2.1 on 2019-11-23 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0002_auto_20191123_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='encuesta',
        ),
    ]
