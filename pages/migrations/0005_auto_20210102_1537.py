# Generated by Django 2.1 on 2021-01-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20210102_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sum',
            name='first',
            field=models.DecimalField(decimal_places=2, error_messages={'required': 'My custom error'}, max_digits=19, null=True),
        ),
    ]