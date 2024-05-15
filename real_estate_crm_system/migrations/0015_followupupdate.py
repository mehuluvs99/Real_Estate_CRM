# Generated by Django 5.0.4 on 2024-05-15 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_crm_system', '0014_alter_add_inquiry_converted_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUpUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('follow_up_date', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, max_length=200, null=True)),
                ('next_follow_up_date', models.CharField(blank=True, max_length=50, null=True)),
                ('converted_date', models.CharField(blank=True, max_length=50, null=True)),
                ('assign_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.assign_to')),
                ('inquiry_stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.inquiry_stage')),
                ('inquiry_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.inquiry_type')),
                ('interested_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.project_name')),
                ('selected_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.selected_unit')),
            ],
        ),
    ]