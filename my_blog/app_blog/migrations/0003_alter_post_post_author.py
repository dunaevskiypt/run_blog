# Generated by Django 3.2 on 2023-11-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_post_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.CharField(default='Unknown Author', max_length=128),
        ),
    ]
