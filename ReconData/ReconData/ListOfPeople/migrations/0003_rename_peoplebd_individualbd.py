# Generated by Django 4.1 on 2024-06-19 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ListOfPeople", "0002_alter_peoplebd_options_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PeopleBd",
            new_name="IndividualBd",
        ),
    ]
