# Generated by Django 4.2.5 on 2023-10-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('auther', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('number_of_pages', models.IntegerField()),
                ('image', models.ImageField(upload_to='static/images/')),
                ('slug', models.SlugField(max_length=200, null=True)),
                ('uploading_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
