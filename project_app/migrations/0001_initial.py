# Generated by Django 3.2 on 2021-05-10 17:44

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('credits', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('role', models.CharField(choices=[('Supervisor', 'Sup'), ('TA', 'Ta'), ('Instructor', 'Ins')], max_length=10)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('officenumber', models.CharField(blank=True, max_length=10)),
                ('officehoursStart', models.TimeField(blank=True, null=True)),
                ('officehoursEnd', models.TimeField(blank=True, null=True)),
                ('officehoursDays', models.CharField(blank=True, max_length=10)),
                ('skills', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graderstatus', models.BooleanField(default=False)),
                ('numlabs', models.IntegerField(default=0)),
                ('assignedlabs', models.IntegerField(default=0)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_app.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionid', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Lecture', 'Lec'), ('Lab', 'Lab'), ('Discussion', 'Disc')], max_length=20)),
                ('scheduleStart', models.TimeField(blank=True, null=True)),
                ('scheduleEnd', models.TimeField(blank=True, null=True)),
                ('scheduleDays', models.CharField(blank=True, max_length=10)),
                ('TA_assigned', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_app.ta')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='Instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_app.user'),
        ),
    ]
