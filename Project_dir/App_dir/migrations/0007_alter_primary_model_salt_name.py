# Generated by Django 4.0 on 2021-12-12 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_dir', '0006_alter_primary_model_drug_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primary_model',
            name='salt_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
