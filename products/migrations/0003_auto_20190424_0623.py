# Generated by Django 2.0.2 on 2019-04-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190424_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]