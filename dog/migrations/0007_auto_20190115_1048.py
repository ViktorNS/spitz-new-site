# Generated by Django 2.1.5 on 2019-01-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0006_dogpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogpicture',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='__image_upload/dog_picture/picture', verbose_name='Picture'),
        ),
    ]