# Generated by Django 2.1 on 2019-11-25 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0006_preguntaresultado_pregunta_denom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='pregunta',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='preguntaresultado',
            name='pregunta_denom',
            field=models.CharField(max_length=100),
        ),
    ]