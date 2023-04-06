# Generated by Django 4.2 on 2023-04-06 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembersHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('serial_number', models.CharField(max_length=6)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logTracker.member')),
            ],
        ),
    ]
