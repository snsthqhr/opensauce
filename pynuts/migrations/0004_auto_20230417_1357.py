# Generated by Django 3.1.3 on 2023-04-17 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pynuts', '0003_gptresponse_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gptresponse',
            old_name='product',
            new_name='explanation',
        ),
    ]
