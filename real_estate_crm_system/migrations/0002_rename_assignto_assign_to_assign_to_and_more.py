# Generated by Django 4.2.2 on 2023-08-20 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_crm_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assign_to',
            old_name='assignto',
            new_name='assign_to',
        ),
        migrations.RenameField(
            model_name='inquiry_stage',
            old_name='inquirystage',
            new_name='inquiry_stage',
        ),
        migrations.RenameField(
            model_name='inquiry_type',
            old_name='inquirytype',
            new_name='inquiry_type',
        ),
        migrations.RenameField(
            model_name='selected_unit',
            old_name='selectedunit',
            new_name='selected_unit',
        ),
    ]
