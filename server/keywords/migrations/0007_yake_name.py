# Generated by Django 3.1.4 on 2020-12-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keywords', '0006_auto_20201227_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='yake',
            name='name',
            field=models.CharField(default='empty', max_length=20),
            preserve_default=False,
        ),
    ]
