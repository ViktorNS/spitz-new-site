# Generated by Django 2.1.5 on 2019-01-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0035_auto_20190126_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybanner',
            name='html_text',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Html text'),
        ),
    ]
