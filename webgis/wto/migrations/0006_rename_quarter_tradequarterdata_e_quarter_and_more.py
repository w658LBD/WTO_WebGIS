# Generated by Django 4.2.8 on 2023-12-21 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wto", "0005_trademonthdata_e_year_trademonthdata_i_year_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tradequarterdata_e",
            old_name="Quarter",
            new_name="quarter",
        ),
        migrations.RenameField(
            model_name="tradequarterdata_i",
            old_name="Quarter",
            new_name="quarter",
        ),
    ]
