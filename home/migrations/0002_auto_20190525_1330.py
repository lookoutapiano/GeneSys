# Generated by Django 2.2.1 on 2019-05-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ContactNumber',
            field=models.IntegerField(),
        ),
    ]