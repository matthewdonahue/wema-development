# Generated by Django 2.2.3 on 2020-06-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]