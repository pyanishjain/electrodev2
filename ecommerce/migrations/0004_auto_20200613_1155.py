# Generated by Django 2.1.5 on 2020-06-13 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_remove_buyerorder_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerorder',
            name='buyerid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.UserProfile'),
        ),
    ]
