# Generated by Django 4.2.2 on 2023-08-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_salary_card_number_alter_salary_cvv'),
    ]

    operations = [
        migrations.CreateModel(
            name='message1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=255)),
                ('sender_id', models.IntegerField(null=True)),
                ('reciever_id', models.IntegerField(null=True)),
                ('current_date', models.DateField(null=True)),
            ],
        ),
    ]