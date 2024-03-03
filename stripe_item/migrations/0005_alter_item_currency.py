# Generated by Django 5.0.2 on 2024-03-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_item', '0004_alter_item_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('USD', 'Usd'), ('EUR', 'Eur')], default='USD', max_length=3),
        ),
    ]
