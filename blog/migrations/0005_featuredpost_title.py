# Generated by Django 3.0.6 on 2020-05-28 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_featuredpost_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredpost',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]