# Generated by Django 3.0.5 on 2020-11-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myR', '0002_auto_20201108_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Student',
        ),
        migrations.RemoveField(
            model_name='student',
            name='credits',
        ),
        migrations.RemoveField(
            model_name='student',
            name='gradelevel',
        ),
        migrations.RemoveField(
            model_name='student',
            name='netId',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ruId',
        ),
        migrations.AddField(
            model_name='course',
            name='Credits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='MeetingType',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='Title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='CoursesRegistered',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='CreditsRegistered',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='CreditsTaken',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='DegreeLevel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='FirstName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='LastName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='RUID',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='netid',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Enrolled',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Index',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='course',
            name='Status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='CoursesTaken',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterModelTable(
            name='course',
            table=None,
        ),
        migrations.AlterModelTable(
            name='student',
            table=None,
        ),
    ]