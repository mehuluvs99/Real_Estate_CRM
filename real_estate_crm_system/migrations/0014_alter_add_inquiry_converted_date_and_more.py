# Generated by Django 5.0.4 on 2024-05-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_crm_system', '0013_alter_add_inquiry_assign_to_alter_add_inquiry_fields_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_inquiry',
            name='converted_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='add_inquiry',
            name='follow_up_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='add_inquiry',
            name='next_follow_up_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
