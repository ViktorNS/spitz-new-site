# Generated by Django 2.1.5 on 2019-01-15 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0016_puppy_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuppyPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='media/__image_upload/dog/puppiesfoto')),
            ],
            options={
                'verbose_name': 'Puppy picture',
            },
        ),
        migrations.RemoveField(
            model_name='puppy',
            name='picture',
        ),
        migrations.AddField(
            model_name='puppypicture',
            name='puppy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='puppy_picture', to='dog.Puppy', verbose_name='Puppy'),
        ),
    ]
