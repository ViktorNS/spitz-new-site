# Generated by Django 2.1.5 on 2019-01-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0008_auto_20190115_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogpicture',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/__image_upload/dog/dogfoto'),
        ),
    ]
