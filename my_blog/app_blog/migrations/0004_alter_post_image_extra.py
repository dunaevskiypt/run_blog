# Generated by Django 3.2 on 2023-11-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_alter_post_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_extra',
            field=models.ImageField(upload_to='masonry'),
        ),
    ]