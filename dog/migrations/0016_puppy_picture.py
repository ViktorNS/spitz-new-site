# Generated by Django 2.1.5 on 2019-01-15 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0015_auto_20190115_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='puppy',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/__image_upload/dog/puppiesfoto'),
        ),
    ]