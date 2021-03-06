# Generated by Django 3.0.8 on 2020-08-06 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_delete_autotest_results_t'),
    ]

    operations = [
        migrations.CreateModel(
            name='settlement_vip_models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_cash_flow', models.CharField(max_length=128)),
                ('book_playCount', models.CharField(max_length=128)),
                ('partner_divide_rate', models.CharField(max_length=128)),
                ('partner_divide_money_final', models.CharField(max_length=128)),
                ('tech_service_consumption', models.CharField(max_length=128)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'VIP会员业务结算结果',
            },
        ),
    ]
