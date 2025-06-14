# Generated by Django 5.1.4 on 2025-01-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_remove_specialoffer_service_specialoffer_services_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='customer_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services_images/'),
        ),
    ]
