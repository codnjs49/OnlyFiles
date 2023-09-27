# Generated by Django 3.2.20 on 2023-08-14 09:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20230809_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiries',
            fields=[
                ('enquiries_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('client_id', models.IntegerField()),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=50, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('reply_time', models.DateTimeField(null=True)),
                ('reply', models.TextField(null=True)),
                ('topic', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'enquiries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Server5',
            fields=[
                ('server5_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_id', models.UUIDField()),
                ('file_version_id', models.UUIDField()),
            ],
            options={
                'db_table': 'server5',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Server5Logs',
            fields=[
                ('server5_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('file_id', models.UUIDField()),
                ('file_version_id', models.UUIDField()),
                ('file_part_id', models.UUIDField()),
                ('delete_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'server5_logs',
                'managed': False,
            },
        ),
    ]
