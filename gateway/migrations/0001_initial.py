# Generated by Django 3.2 on 2021-09-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('gateway_request_url', models.CharField(blank=True, max_length=150, verbose_name='request url')),
                ('gateway_verify_url', models.CharField(blank=True, max_length=150, verbose_name='verify url')),
                ('gateway_code', models.CharField(choices=[('zarrinpal', 'Zarrinpal'), ('saman', 'Saman')], max_length=20, verbose_name='gateway code')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('auth_data', models.TextField(blank=True, verbose_name='auth data')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
