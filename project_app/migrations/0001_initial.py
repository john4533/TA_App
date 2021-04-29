# Generated by Django 3.1.7 on 2021-04-29 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.CharField(max_length=20)),
                ('coursename', models.CharField(max_length=50)),
                ('coursecredits', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('role', models.CharField(choices=[('Supervisor', 'Sup'), ('TA', 'Ta'), ('Instructor', 'Ins')], max_length=10)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('officehours', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionid', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Lecture', 'Lec'), ('Lab', 'Lab'), ('Discussion', 'Disc')], max_length=20)),
                ('schedule', models.CharField(blank=True, max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='user_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project_app.user'),
        ),
    ]
