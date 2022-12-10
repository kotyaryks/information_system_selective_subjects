from django.contrib.auth.models import User
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
        on_delete=models.CASCADE
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
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.code} {self.education_program}"

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"


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
        blank=False
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"


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

class Subject(models.Model):
    LEVEL = (
        ('b', 'перший(бакалаврський)'),
        ('m', 'другий(магістерський)'),
        ('p', 'третій(освітньо-науковий)'),
    )
    name = models.CharField(
        "Назва дисципліни",
        max_length=100,
        blank=False
    )
    majoring = models.ManyToManyField(
        Majoring,
        verbose_name="Рекомендується для галузі знань "
                     "(спеціальності, освітньої програми)",
    )
    department = models.ForeignKey(
        Department,
        verbose_name="Кафедра",
        on_delete=models.CASCADE,
    )
    lecturer = models.ManyToManyField(Lecturer, blank=True)
    level = models.CharField(
        "Рівень ВО",
        max_length=1,
        choices=LEVEL,
        default='b',
    )
    semester = models.ManyToManyField(Semester, blank=False)
    language = models.CharField(
        "Мова викладання",
        blank=False,
        max_length=30,
        default="українська"
    )
    preconditions = models.TextField(
        "Пререквізити (передумови вивчення дисципліни)",
        blank=False,
        max_length=120,
        default="Немає"
    )
    what_is_being_studied = models.TextField(
        "Що буде вивчатися",
        blank=False,
        max_length=150,
    )
    why_should_be_studied = models.TextField(
        "Чому це цікаво/треба вивчати",
        blank=False,
        max_length=150,
    )
    what_can_be_learned = models.TextField(
        "Чого можна навчитися (результати навчання)",
        blank=False,
        max_length=180,
    )
    how_to_use = models.TextField(
        "Як можна користуватися набутими знаннями і уміннями (компетентності)",
        blank=False,
        max_length=150,
    )
    information_provision = models.TextField(
        "Інформаційне забезпечення",
        blank=False,
        max_length=150,
    )
    educational_activities_type = models.CharField(
        "Види навчальних занять (лекції, практичні, семінарські, лабораторні заняття тощо",
        blank=False,
        max_length=100,
    )
    semester_control_type = models.CharField(
        "Вид семестрового контролю",
        blank=False,
        max_length=30,
    )
    max_capacity = models.PositiveSmallIntegerField("Максимальна кількість здобувачів", blank=True)
    min_capacity = models.PositiveSmallIntegerField("Мінімальна кількість здобувачів", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вибіркова дисципліна"
        verbose_name_plural = "Вибіркові дисципліни"

