# Generated by Django 3.1.2 on 2020-11-02 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='PhotoFileName',
        ),
        migrations.AddField(
            model_name='employees',
            name='DateOfBirth',
            field=models.DateField(default='1950-01-01'),
        ),
        migrations.AddField(
            model_name='employees',
            name='Designation',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='employees',
            name='EmailId',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='employees',
            name='Location',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='employees',
            name='MobileNo',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='employees',
            name='DateOfJoining',
            field=models.DateField(default='1950-01-01'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Department',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='employees',
            name='EmployeeName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
