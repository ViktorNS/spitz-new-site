# Generated by Django 2.1.5 on 2019-01-15 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0026_photogallery_gellery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Contact',
            },
        ),
    ]
