# Generated by Django 4.2.2 on 2023-08-20 08:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assign_To',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignto', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry_Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquirystage', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inquiry_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquirytype', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_terms', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Selected_Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectedunit', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_receive', models.CharField(blank=True, max_length=100, null=True)),
                ('gst', models.CharField(blank=True, max_length=100, null=True)),
                ('current_outstanding', models.CharField(blank=True, max_length=100, null=True)),
                ('unique_key', models.CharField(blank=True, max_length=100, null=True)),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.payment_type')),
            ],
        ),
        migrations.CreateModel(
            name='Add_Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('whatsapp_mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.CharField(blank=True, max_length=500, null=True)),
                ('converted_date', models.DateTimeField(blank=True, max_length=100, null=True)),
                ('unique_key', models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=100)),
                ('assign_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.assign_to')),
                ('fields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.fields')),
                ('inquiry_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.inquiry_stage')),
                ('inquiry_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.inquiry_type')),
                ('interested_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.project_name')),
                ('selected_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.selected_unit')),
            ],
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('whatsapp_mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('sq_ft', models.CharField(blank=True, max_length=100, null=True)),
                ('sq_meter', models.CharField(blank=True, max_length=100, null=True)),
                ('rate_per_ft', models.CharField(blank=True, max_length=100, null=True)),
                ('rate_per_meter', models.CharField(blank=True, max_length=100, null=True)),
                ('cash', models.CharField(blank=True, max_length=100, null=True)),
                ('gst', models.CharField(blank=True, max_length=100, null=True)),
                ('total_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('due_date', models.CharField(blank=True, max_length=100, null=True)),
                ('unique_key', models.CharField(blank=True, max_length=100, null=True)),
                ('interested_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.project_name')),
                ('payment_terms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.payment_terms')),
                ('selected_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.selected_unit')),
            ],
        ),
    ]
