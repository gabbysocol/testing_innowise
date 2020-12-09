# Generated by Django 3.1.4 on 2020-12-09 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.TextField()),
                ('speciality', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='employee.company')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partnership', models.CharField(max_length=255)),
                ('from_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_partner1', to='employee.company')),
                ('with_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_partner2', to='employee.company')),
            ],
        ),
    ]
