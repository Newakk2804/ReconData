from django.db import models


class IndividualBd(models.Model):
    firstName = models.CharField(max_length=25, verbose_name="Фамилия", null=True)
    name = models.CharField(max_length=25, verbose_name="Имя", null=True)
    lastName = models.CharField(max_length=25, verbose_name="Отчество", null=True)
    dateOfBirth = models.DateField(
        auto_now=False, verbose_name="Дата рождения", null=True
    )
    location = models.CharField(
        max_length=100, verbose_name="Место жительства", null=True
    )
    docType = models.CharField(max_length=20, verbose_name="Вид документа", null=True)
    passportIdNumber = models.CharField(
        max_length=15, verbose_name="Идентификационный номер паспорта", null=True
    )
    passportSeries = models.CharField(
        max_length=10, verbose_name="Серия паспорта", null=True
    )
    issuedBy = models.CharField(
        max_length=150, verbose_name="Кем выдан документ", null=True
    )
    dateIssuedBy = models.DateField(
        auto_now=False, verbose_name="Дата выдачи документа", null=True
    )
    email = models.CharField(
        max_length=50, verbose_name="Адрес электронной почты", null=True
    )
    numberPhone = models.CharField(
        max_length=15, verbose_name="Номер телефона", null=True
    )

    def __str__(self):
        return f"{self.firstName} {self.name} {self.lastName}"

    class Meta:
        verbose_name = "физическое лицо"
        verbose_name_plural = "физические лица"


class IndividEnter(models.Model):
    firstName = models.CharField(max_length=25, verbose_name="Фамилия", null=True)
    name = models.CharField(max_length=25, verbose_name="Имя", null=True)
    lastName = models.CharField(max_length=25, verbose_name="Отчество", null=True)
    dateOfBirth = models.DateField(
        auto_now=False, verbose_name="Дата рождения", null=True
    )
    location = models.CharField(
        max_length=100, verbose_name="Место жительства", null=True
    )
    docType = models.CharField(max_length=20, verbose_name="Вид документа", null=True)
    passportIdNumber = models.CharField(
        max_length=15, verbose_name="Идентификационный номер паспорта", null=True
    )
    passportSeries = models.CharField(
        max_length=10, verbose_name="Серия паспорта", null=True
    )
    issuedBy = models.CharField(
        max_length=150, verbose_name="Кем выдан документ", null=True
    )
    dateIssuedBy = models.DateField(
        auto_now=False, verbose_name="Дата выдачи документа", null=True
    )
    email = models.CharField(
        max_length=50, verbose_name="Адрес электронной почты", null=True
    )
    numberPhone = models.CharField(
        max_length=15, verbose_name="Номер телефона", null=True
    )
    numberStateRegist = models.CharField(
        max_length=20, verbose_name="Номер государственной регистрации", null=True
    )
    nameOfCompanyRegist = models.CharField(
        max_length=50, verbose_name="Наименование организации, осуществившей государственную регистрацию", null=True
    )
    dateRegist = models.DateField(
        auto_now=False, verbose_name="Дата регистрации", null=True
    )
    decisionNumber = models.CharField(
        max_length=25, verbose_name="Номер решения", null=True
    )

    def __str__(self):
        return f"{self.numberStateRegist} {self.firstName}"

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"


class LegalPerson(models.Model):
    nameOfCompany = models.CharField(
        max_length=100, verbose_name="Наименование организации", null=True
    )
    locationOfTheCompany = models.CharField(
        max_length=100, verbose_name="Адрес организации", null=True
    )
    numberStateRegist = models.CharField(
        max_length=20, verbose_name="Номер государственной регистрации", null=True
    )
    nameOfCompanyRegist = models.CharField(
        max_length=50, verbose_name="Наименование организации, осуществившей государственную регистрацию", null=True
    )
    dateRegist = models.DateField(
        auto_now=False, verbose_name="Дата регистрации", null=True
    )
    decisionNumber = models.CharField(
        max_length=25, verbose_name="Номер решения", null=True
    )
    payerAccNumber = models.CharField(
        max_length=20, verbose_name="Учетный номер плательщика", null=True
    )
    email = models.CharField(
        max_length=50, verbose_name="Адрес электронной почты", null=True
    )
    numberPhone = models.CharField(
        max_length=15, verbose_name="Контактный телефон", null=True
    )
    firstNameMan = models.CharField(
        max_length=25, verbose_name="Фамилия руководителя", null=True
    )
    nameMan = models.CharField(
        max_length=25, verbose_name="Имя руководителя", null=True
    )
    lastNameMan = models.CharField(
        max_length=25, verbose_name="Отчество руководителя", null=True
    )

    def __str__(self):
        return f"{self.nameOfCompany} {self.numberStateRegist}"

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"
