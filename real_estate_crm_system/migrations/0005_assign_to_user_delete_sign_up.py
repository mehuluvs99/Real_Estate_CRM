# Generated by Django 4.2.2 on 2023-08-20 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_crm_system', '0004_sign_up_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign_To_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fields', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.fields')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_crm_system.project_name')),
            ],
        ),
        migrations.DeleteModel(
            name='Sign_up',
        ),
    ]