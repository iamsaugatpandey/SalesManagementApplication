# Generated by Django 3.1.1 on 2020-10-06 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20201006_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='customer',
            name='email_address',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='Name', max_length=120, unique=True),
        ),
    ]