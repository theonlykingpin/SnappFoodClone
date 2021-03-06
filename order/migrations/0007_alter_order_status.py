# Generated by Django 3.2.8 on 2021-10-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_merge_0003_alter_order_status_0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'preparing food'), (1, 'sending'), (2, 'delivered')], default=0, verbose_name='status'),
        ),
    ]
