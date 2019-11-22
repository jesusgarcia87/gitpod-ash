# Generated by Django 2.2.7 on 2019-11-21 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(default='n/a', max_length=100)),
                ('location', models.CharField(default='n/a', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bank.Branch')),
                ('product_username', models.CharField(max_length=40)),
                ('product_email', models.EmailField(max_length=400)),
                ('product_options', models.CharField(choices=[('account', 'Account'), ('checking', 'Checking'), ('balance', 'Balance')], default=('account', 'Account'), max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bank.Branch')),
                ('product', models.EmailField(max_length=400)),
                ('product_options', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Branch')),
            ],
        ),
    ]
