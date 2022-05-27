# Generated by Django 4.0.4 on 2022-05-27 06:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomForm',
            fields=[
                ('form_id', models.AutoField(primary_key=True, serialize=False)),
                ('form_title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 27, 6, 18, 48, 886412, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='FormFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('field_description', models.CharField(max_length=100)),
                ('field_type', models.CharField(choices=[('0', 'Text'), ('1', 'Textarea'), ('2', 'Select')], default=None, max_length=10, null=True)),
                ('field_choices', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 27, 6, 18, 48, 886412, tzinfo=utc))),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.customform')),
            ],
        ),
    ]
