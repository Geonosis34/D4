# Generated by Django 3.2.8 on 2021-11-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0005_alter_newsmodel_datecreation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
