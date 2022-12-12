from django.db import models


class Faculty(models.Model):
    name = models.CharField(
        "Назва факультету",
        blank=False,
        max_length=100
    )
    short_name = models.CharField(
        "Абревіатура",
        blank=False,
        max_length=10
    )

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "Факультет"
        verbose_name_plural = "Факультети"


class Department(models.Model):
    name = models.CharField(
        "Кафедра",
        blank=False,
        max_length=100
    )
    faculty = models.ForeignKey(
        Faculty,
        verbose_name="Факультет",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"


class Majoring(models.Model):
    code = models.PositiveSmallIntegerField("Шифр")
    name = models.CharField(
        "Назва спеціальності",
        blank=False,
        max_length=100
    )
    education_program = models.CharField(
        "Освітня програма",
        blank=False,
        max_length=100
    )
    department = models.ForeignKey(
        Department,
        verbose_name="Кафедра",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.code} {self.education_program}"

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"


class Semester(models.Model):
    semester = models.CharField(
        "Семестр",
        max_length=30,
        blank=False
    )

    def __str__(self):
        return self.semester

    class Meta:
        verbose_name = "Семестр"
        verbose_name_plural = "Семестри"


class AcademicYear(models.Model):
    text = models.CharField(
        "Навчальний рік",
        blank=False,
        max_length=9,
    )
    deadline = models.DateField(verbose_name="Термін вибору дисциплін", auto_now=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Навчальний рік"
        verbose_name_plural = "Навчальні роки"
