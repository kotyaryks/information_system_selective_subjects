from django.contrib.auth.models import User
from django.db import models
from uni_structure.models import Department, Majoring

class Lecturer(models.Model):
    username = models.OneToOneField(
        User,
        verbose_name="Ім'я користувача",
        on_delete=models.CASCADE,
        blank=False
    )
    last_name = models.CharField(
        "Прізвище",
        max_length=30,
        blank=False
    )
    first_name = models.CharField(
        "Ім'я",
        max_length=30,
        blank=False
    )
    patronymic = models.CharField(
        "По батькові",
        max_length=30,
        blank=True
    )
    department = models.ForeignKey(
        Department,
        verbose_name="Кафедра",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"


class Student(models.Model):
    LEVEL = (
        ('b', 'перший(бакалаврський)'),
        ('m', 'другий(магістерський)'),
        ('p', 'третій(освітньо-науковий)'),
    )

    username = models.OneToOneField(
        User,
        verbose_name="Ім'я користувача",
        on_delete=models.CASCADE,
        blank=False
    )
    last_name = models.CharField(
        "Прізвище",
        max_length=30,
        blank=False
    )
    first_name = models.CharField(
        "Ім'я",
        max_length=30,
        blank=False
    )
    patronymic = models.CharField(
        "По батькові",
        max_length=30,
        blank=True
    )
    level = models.CharField(
        "Рівень ВО",
        max_length=1,
        choices=LEVEL,
        default='b',
    )
    majoring = models.ForeignKey(
        Majoring,
        verbose_name="Спеціальність",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = "Студента"
        verbose_name_plural = "Студенти"

