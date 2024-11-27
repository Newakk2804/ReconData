# Generated by Django 4.1 on 2024-06-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ListOfPeople", "0003_rename_peoplebd_individualbd"),
    ]

    operations = [
        migrations.AddField(
            model_name="individualbd",
            name="dateIssuedBy",
            field=models.DateField(null=True, verbose_name="Дата выдачи документа"),
        ),
        migrations.AddField(
            model_name="individualbd",
            name="docType",
            field=models.CharField(
                max_length=20, null=True, verbose_name="Вид документа"
            ),
        ),
        migrations.AddField(
            model_name="individualbd",
            name="email",
            field=models.CharField(
                max_length=50, null=True, verbose_name="Адрес электронной почты"
            ),
        ),
        migrations.AddField(
            model_name="individualbd",
            name="issuedBy",
            field=models.CharField(
                max_length=150, null=True, verbose_name="Кем выдан документ"
            ),
        ),
        migrations.AddField(
            model_name="individualbd",
            name="location",
            field=models.CharField(
                max_length=100, null=True, verbose_name="Место жительства"
            ),
        ),
        migrations.AddField(
            model_name="individualbd",
            name="numberPhone",
            field=models.CharField(
                max_length=15, null=True, verbose_name="Номер телефона"
            ),
        ),
        migrations.AlterField(
            model_name="individualbd",
            name="dateOfBirth",
            field=models.DateField(null=True, verbose_name="Дата рождения"),
        ),
        migrations.AlterField(
            model_name="individualbd",
            name="firstName",
            field=models.CharField(max_length=25, null=True, verbose_name="Фамилия"),
        ),
        migrations.AlterField(
            model_name="individualbd",
            name="lastName",
            field=models.CharField(max_length=25, null=True, verbose_name="Отчество"),
        ),
        migrations.AlterField(
            model_name="individualbd",
            name="name",
            field=models.CharField(max_length=25, null=True, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="individualbd",
            name="passportIdNumber",
            field=models.CharField(
                max_length=15,
                null=True,
                verbose_name="Идентификационный номер паспорта",
            ),
        ),
        migrations.AlterField(
            model_name="individualbd",
            name="passportSeries",
            field=models.CharField(
                max_length=10, null=True, verbose_name="Серия паспорта"
            ),
        ),
    ]
