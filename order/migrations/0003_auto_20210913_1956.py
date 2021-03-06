# Generated by Django 3.2 on 2021-09-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210913_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_delivered',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'preparing food'), (0, 'sending'), (2, 'delivered')], default=0, verbose_name='status'),
        ),
    ]
