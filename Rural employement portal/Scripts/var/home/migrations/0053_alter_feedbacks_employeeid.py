# Generated by Django 4.2.2 on 2023-09-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_alter_feedbacks_employeeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='employeeid',
            field=models.CharField(max_length=25),
        ),
    ]