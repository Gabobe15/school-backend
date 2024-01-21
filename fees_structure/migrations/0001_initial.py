# Generated by Django 4.1 on 2023-10-06 20:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeesStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_reg', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
