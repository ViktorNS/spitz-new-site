# Generated by Django 2.1.5 on 2019-03-30 23:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0047_auto_20190315_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='home_text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Home text'),
        ),
        migrations.AddField(
            model_name='content',
            name='home_text_et',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Home text'),
        ),
        migrations.AddField(
            model_name='content',
            name='home_text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Home text'),
        ),
        migrations.AddField(
            model_name='new',
            name='news_text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='News text'),
        ),
        migrations.AddField(
            model_name='new',
            name='news_text_et',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='News text'),
        ),
        migrations.AddField(
            model_name='new',
            name='news_text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='News text'),
        ),
        migrations.AddField(
            model_name='new',
            name='title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='new',
            name='title_et',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='new',
            name='title_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='puppy',
            name='status_en',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Sold', 'Sold')], max_length=9, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='puppy',
            name='status_et',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Sold', 'Sold')], max_length=9, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='puppy',
            name='status_ru',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Sold', 'Sold')], max_length=9, null=True, verbose_name='Status'),
        ),
    ]