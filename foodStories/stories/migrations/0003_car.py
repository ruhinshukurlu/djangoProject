# Generated by Django 3.0.6 on 2020-07-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20200701_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('image', models.URLField(verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
    ]
