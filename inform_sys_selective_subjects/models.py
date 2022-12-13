from django.db import models
from info_sys_users.models import Lecturer, Student
from uni_structure.models import Faculty, Department, AcademicYear, Majoring, Semester


class Subject(models.Model):
    LEVEL = (
        ('b', 'перший(бакалаврський)'),
        ('m', 'другий(магістерський)'),
        ('p', 'третій(освітньо-науковий)'),
    )
    PART = (
        ('u', 'університетська'),
        ('f', 'факультетська'),
    )

    part = models.CharField(
        "Університетська\факультетська",
        max_length=1,
        choices=PART,
        default='u',
    )
    code = models.CharField(
        "Код дисципліни",
        max_length=10,
        blank=False
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
    lecturer = models.ManyToManyField(Lecturer,verbose_name="П.І.П. НПП (за можливості)", blank=True)
    level = models.CharField(
        "Рівень ВО",
        max_length=1,
        choices=LEVEL,
        default='b',
    )
    semester = models.ManyToManyField(Semester,verbose_name="Семестр", blank=False)
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
    semester_control_type = models.CharField(
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
        return f"{self.code} {self.name}"

    class Meta:
        verbose_name = "Вибіркова дисципліна"
        verbose_name_plural = "Вибіркові дисципліни"


class SelectedSubjectsByStudentList(models.Model):
    subjects = models.ManyToManyField(Subject, blank=False)
    students = models.ForeignKey(
        Student,
        verbose_name="Студент",
        on_delete=models.CASCADE,
    )
    academic_year = models.ForeignKey(
        AcademicYear,
        verbose_name="Навчальний рік",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.academic_year} - {self.students}"

    class Meta:
        verbose_name = "Обрані студентом дисципліни"
        verbose_name_plural = "Обрані студентами дисципліни"
