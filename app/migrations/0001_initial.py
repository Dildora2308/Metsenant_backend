# Generated by Django 5.1.2 on 2024-10-28 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('phone_number', models.IntegerField(max_length=13)),
                ('donation_amount', models.PositiveBigIntegerField()),
                ('org_name', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('personal', 'jismoniy shaxs'), ('legal', 'yuridik shaxs')], max_length=250)),
                ('status', models.CharField(choices=[('New', 'yangi'), ('Modeartion', 'Moderatsiya'), ('confirmed', 'Tasdiqlangan'), ('cancelled', 'Bekor qilingan')], default='New', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment_type', models.CharField(choices=[('Cash', 'Naqd'), ('credit card', 'Plastik karta')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('student_type', models.CharField(choices=[('Bachelor', 'Bakalavr'), ('Master', 'Magistr')], max_length=250)),
                ('contract_amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.sponsor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.university'),
        ),
    ]