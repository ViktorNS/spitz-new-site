# Generated by Django 2.1.5 on 2019-01-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0028_auto_20190115_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='mybanner',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Name'),
        ),
    ]
