# Generated by Django 4.2.7 on 2023-11-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_contact', models.CharField(max_length=20)),
                ('user_rollnum', models.CharField(max_length=20)),
                ('course_option', models.CharField(choices=[('BSC(cs)', 'BSC(cs)'), ('B.Tech(CS)', 'B.Tech(CS)'), ('MCA', 'MCA'), ('Other', 'Other')], max_length=20)),
                ('topic', models.CharField(choices=[('C Language', 'C Language'), ('C++', 'C++'), ('Java', 'Java'), ('Web Development', 'Web Development'), ('Data Science', 'Data Science'), ('MySQL', 'MySQL'), ('Python-Programming', 'Python-Programming'), ('Data Structure and Algorithm', 'Data Structure and Algorithm')], max_length=50)),
                ('interview_date', models.DateField()),
                ('resume', models.FileField(upload_to='resumes/')),
                ('video', models.FileField(upload_to='videos/')),
                ('suggestions', models.TextField()),
            ],
        ),
    ]
