# Generated by Django 2.1.4 on 2018-12-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='site_url',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]