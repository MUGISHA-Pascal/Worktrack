# Generated by Django 4.2.9 on 2024-05-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeemanagement', '0006_delete_profileimagedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='perfomancedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfomance', models.CharField(max_length=128)),
                ('perfomancedate', models.DateField()),
            ],
        ),
    ]
