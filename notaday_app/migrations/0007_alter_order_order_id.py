# Generated by Django 5.0.4 on 2024-05-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notaday_app', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
