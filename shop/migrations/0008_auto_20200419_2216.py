# Generated by Django 3.0.4 on 2020-04-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200419_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='msg_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
