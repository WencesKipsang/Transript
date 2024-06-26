# Generated by Django 4.2.5 on 2023-09-16 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_year2_grade_1_alter_year2_grade_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_with_course', to='student.course'),
        ),
        migrations.AlterField(
            model_name='units',
            name='unit_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='year2',
            name='remark',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='year2',
            name='sub_1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='year2',
            name='sub_2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='year2',
            name='sub_3',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='year2',
            name='sub_4',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='year2',
            name='sub_5',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='year2',
            name='sub_6',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='year2',
            name='sub_7',
            field=models.CharField(max_length=200),
        ),
    ]
