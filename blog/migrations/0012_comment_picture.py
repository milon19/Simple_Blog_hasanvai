# Generated by Django 3.0.6 on 2020-05-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='picture',
            field=models.ImageField(default='default/comments_author.jpg', upload_to='comments_author/'),
        ),
    ]