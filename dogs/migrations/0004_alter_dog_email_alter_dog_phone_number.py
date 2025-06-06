# Generated by Django 5.1.4 on 2025-01-19 22:24

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_dog_email_dog_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='email',
            field=models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator(message='Invalid email format.')]),
        ),
        migrations.AlterField(
            model_name='dog',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Enter a valid international phone number (e.g., +1234567890).', max_length=128, null=True, region=None),
        ),
    ]
