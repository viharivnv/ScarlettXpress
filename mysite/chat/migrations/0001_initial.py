# Generated by Django 3.0.5 on 2020-11-08 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseID', models.CharField(blank=True, max_length=10, null=True)),
                ('Index', models.IntegerField(blank=True, null=True)),
                ('Title', models.CharField(blank=True, max_length=500, null=True)),
                ('Instructors', models.CharField(max_length=500)),
                ('Credits', models.IntegerField(default=None)),
                ('MeetingType', models.CharField(blank=True, max_length=100, null=True)),
                ('Status', models.BooleanField(default=True)),
                ('Enrolled', models.IntegerField(blank=True, null=True)),
                ('Capacity', models.IntegerField(blank=True, null=True)),
                ('MeetingTimes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netID', models.CharField(blank=True, max_length=10, null=True)),
                ('RUID', models.IntegerField(blank=True, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=50, null=True)),
                ('LastName', models.CharField(blank=True, max_length=50, null=True)),
                ('DegreeLevel', models.CharField(blank=True, max_length=50, null=True)),
                ('CreditsRegistered', models.IntegerField(blank=True, null=True)),
                ('CreditsTaken', models.IntegerField(blank=True, null=True)),
                ('CoursesRegistered', models.IntegerField(blank=True, null=True)),
                ('CoursesTaken', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.CharField(max_length=10)),
                ('message_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Conversation')),
            ],
        ),
    ]
