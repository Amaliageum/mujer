# Generated by Django 2.1 on 2019-12-08 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0007_auto_20191125_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='tipo',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]