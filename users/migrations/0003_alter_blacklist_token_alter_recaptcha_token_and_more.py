# Generated by Django 5.1.5 on 2025-01-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_blacklist_token_alter_recaptcha_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklist',
            name='token',
            field=models.CharField(max_length=44),
        ),
        migrations.AlterField(
            model_name='recaptcha',
            name='token',
            field=models.CharField(max_length=44),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='token',
            field=models.CharField(max_length=44),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=44),
        ),
    ]
