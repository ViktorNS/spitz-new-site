# Generated by Django 2.1.5 on 2019-01-15 13:17

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('dog', '0017_auto_20190115_1243'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PuppieGroup',
            new_name='PuppieParents',
        ),
        migrations.AlterModelOptions(
            name='puppieparents',
            options={'verbose_name': 'Puppie parents'},
        ),
    ]
