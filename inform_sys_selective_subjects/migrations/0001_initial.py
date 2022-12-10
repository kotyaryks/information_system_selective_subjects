# Generated by Django 4.1.4 on 2022-12-10 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедри',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва факультету')),
                ('short_name', models.CharField(max_length=10, verbose_name='Абревіатура')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультети',
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=30, verbose_name='Семестр')),
            ],
            options={
                'verbose_name': 'Семестр',
                'verbose_name_plural': 'Семестри',
            },
        ),
        migrations.CreateModel(
            name='Majoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveSmallIntegerField(verbose_name='Шифр')),
                ('name', models.CharField(max_length=100, verbose_name='Назва спеціальності')),
                ('education_program', models.CharField(max_length=100, verbose_name='Освітня програма')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inform_sys_selective_subjects.department', verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Спеціальність',
                'verbose_name_plural': 'Спеціальності',
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30, verbose_name='Прізвище')),
                ('first_name', models.CharField(max_length=30, verbose_name="Ім'я")),
                ('patronymic', models.CharField(max_length=30, verbose_name='По батькові')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Ім'я користувача")),
            ],
            options={
                'verbose_name': 'Викладач',
                'verbose_name_plural': 'Викладачі',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inform_sys_selective_subjects.faculty', verbose_name='Факультет'),
        ),
    ]
