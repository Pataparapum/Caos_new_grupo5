# Generated by Django 5.0.6 on 2024-07-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subir_noticias', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='fecha_creacion',
            new_name='fecha_publicacion',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.CharField(choices=[('policial', 'Policial'), ('economia', 'Economía'), ('deportes', 'Deportes'), ('ciencia_tecnologia', 'Ciencia y Tecnología'), ('internacional', 'Internacional')], max_length=50),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='ubicacion',
            field=models.CharField(max_length=100),
        ),
    ]
