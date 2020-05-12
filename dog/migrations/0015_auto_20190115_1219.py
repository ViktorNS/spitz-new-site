# Generated by Django 2.1.5 on 2019-01-15 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0014_auto_20190115_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuppieGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
                ('dad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='dog.Boy', verbose_name='Dad')),
                ('mom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='dog.Girl', verbose_name='Mom')),
            ],
            options={
                'verbose_name': 'Puppie group',
            },
        ),
        migrations.RemoveField(
            model_name='puppy',
            name='dad',
        ),
        migrations.RemoveField(
            model_name='puppy',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='puppy',
            name='mom',
        ),
        migrations.AddField(
            model_name='puppy',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='dog.PuppieGroup', verbose_name='Group'),
        ),
    ]