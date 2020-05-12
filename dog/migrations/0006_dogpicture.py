# Generated by Django 2.1.5 on 2019-01-15 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0005_auto_20190115_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Picture')),
                ('dog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dog_pictures', to='dog.Dog', verbose_name='Dog')),
            ],
            options={
                'verbose_name': 'Dog picture',
            },
        ),
    ]