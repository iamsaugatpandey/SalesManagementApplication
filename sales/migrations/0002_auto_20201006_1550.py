# Generated by Django 3.1.1 on 2020-10-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(default='jdoe@fashion.com', max_length=120),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='Joe', max_length=120),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='Doe', max_length=120),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
