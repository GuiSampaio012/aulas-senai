# Generated by Django 4.2.1 on 2023-06-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backPalmeiras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='produtos'),
        ),
    ]
