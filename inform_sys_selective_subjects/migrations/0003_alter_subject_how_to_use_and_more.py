# Generated by Django 4.1.4 on 2022-12-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inform_sys_selective_subjects', '0002_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='how_to_use',
            field=models.TextField(max_length=150, verbose_name='Як можна користуватися набутими знаннями і уміннями (компетентності)'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='information_provision',
            field=models.TextField(max_length=150, verbose_name='Інформаційне забезпечення'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='preconditions',
            field=models.TextField(default='Немає', max_length=120, verbose_name='Пререквізити (передумови вивчення дисципліни)'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='what_can_be_learned',
            field=models.TextField(max_length=180, verbose_name='Чого можна навчитися (результати навчання)'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='what_is_being_studied',
            field=models.TextField(max_length=150, verbose_name='Що буде вивчатися'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='why_should_be_studied',
            field=models.TextField(max_length=150, verbose_name='Чому це цікаво/треба вивчати'),
        ),
    ]