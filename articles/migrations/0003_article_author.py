# Generated by Django 2.0.3 on 2018-04-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
    ]
