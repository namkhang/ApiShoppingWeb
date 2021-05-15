# Generated by Django 3.2.1 on 2021-05-13 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('idstore', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('idowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.storeowner')),
            ],
            options={
                'db_table': 'store',
            },
        ),
    ]