# Generated by Django 5.0.6 on 2024-07-14 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agregarproductos',
            name='nombre',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agregarproductos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]