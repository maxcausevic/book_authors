# Generated by Django 2.2.4 on 2021-03-22 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20210322_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='some String'),
            preserve_default=False,
        ),
    ]
