# Generated by Django 5.0.4 on 2024-05-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_crm_system', '0015_followupupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='followupupdate',
            name='unique_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
