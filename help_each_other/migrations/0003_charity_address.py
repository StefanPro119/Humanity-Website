# Generated by Django 3.1.5 on 2021-10-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help_each_other', '0002_auto_20210924_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]