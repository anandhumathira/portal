# Generated by Django 4.2.2 on 2023-09-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_workemployee_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workemployee',
            name='payment_status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]