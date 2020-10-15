# Generated by Django 3.1.1 on 2020-10-15 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=50, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Joe', max_length=120)),
                ('last_name', models.CharField(default='Doe', max_length=120)),
                ('email', models.CharField(default='jdoe@fashion.com', max_length=120, unique=True)),
                ('address', models.CharField(max_length=220)),
                ('phone', models.CharField(max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('website', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('price', models.PositiveIntegerField(default=1)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.color')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.type')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('decline', 'Decline'), ('complete', 'Complete')], max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.product')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_in_person', models.BooleanField(default=True)),
                ('courier_name', models.CharField(max_length=120)),
                ('pickup_name', models.CharField(default='Mary Howl', max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.order')),
            ],
        ),
    ]
