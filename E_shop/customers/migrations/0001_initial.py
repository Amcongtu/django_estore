# Generated by Django 4.0.6 on 2022-10-22 05:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=400, null=True)),
                ('image', models.ImageField(default='users/customers/noavatar.png', upload_to='users/customers')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Customer_role', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='customers.customer_role')),
            ],
        ),
    ]
