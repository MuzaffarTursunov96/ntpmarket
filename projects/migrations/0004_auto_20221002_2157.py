# Generated by Django 2.2.14 on 2022-10-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20221002_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
