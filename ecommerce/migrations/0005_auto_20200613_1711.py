# Generated by Django 2.1.5 on 2020-06-13 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20200613_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='houseno',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='ward',
            field=models.CharField(max_length=100, null=True),
        ),
    ]