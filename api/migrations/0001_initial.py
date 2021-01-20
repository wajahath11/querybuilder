# Generated by Django 2.2.8 on 2021-01-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=20)),
                ('account_number', models.IntegerField()),
                ('customer_account', models.CharField(max_length=20)),
                ('tran_date', models.DateTimeField()),
                ('branch_code', models.CharField(max_length=20)),
                ('tran_ref_no', models.CharField(max_length=20)),
                ('acc_entry_sr_no', models.IntegerField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]