# Generated by Django 3.0.8 on 2020-09-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20200815_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcases',
            name='case_type',
            field=models.CharField(default='app', max_length=64),
        ),
    ]