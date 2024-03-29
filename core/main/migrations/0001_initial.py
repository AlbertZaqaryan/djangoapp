# Generated by Django 5.0.1 on 2024-01-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Product name')),
                ('price', models.PositiveIntegerField(verbose_name='Product price')),
                ('description', models.TextField(verbose_name='Product description')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Product image')),
            ],
        ),
    ]
