# Generated by Django 3.2.14 on 2022-08-01 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220731_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='prispevok',
            name='userId',
            field=models.IntegerField(default=True),
        ),
    ]