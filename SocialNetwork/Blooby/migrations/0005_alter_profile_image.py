# Generated by Django 3.2.14 on 2022-08-31 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blooby', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
