# Generated by Django 3.2 on 2023-11-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0004_alter_post_image_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_2',
            field=models.ImageField(upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_extra',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
