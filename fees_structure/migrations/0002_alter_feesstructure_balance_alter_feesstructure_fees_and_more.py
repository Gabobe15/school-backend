# Generated by Django 4.1 on 2023-10-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees_structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feesstructure',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feesstructure',
            name='fees',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feesstructure',
            name='payment',
            field=models.IntegerField(null=True),
        ),
    ]