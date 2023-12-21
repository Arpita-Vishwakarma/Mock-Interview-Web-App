from django.db import models

class InterviewInformation(models.Model):
    COURSE_OPTIONS = [
        ('BSC(cs)', 'BSC(cs)'),
        ('B.Tech(CS)', 'B.Tech(CS)'),
        ('MCA', 'MCA'),
        ('Other', 'Other'),
    ]

    TOPIC_CHOICES = [
        ('C Language', 'C Language'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Web Development', 'Web Development'),
        ('Data Science', 'Data Science'),
        ('MySQL', 'MySQL'),
        ('Python-Programming', 'Python-Programming'),
        ('Data Structure and Algorithm', 'Data Structure and Algorithm'),
    ]

    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_contact = models.CharField(max_length=20)
    user_rollnum = models.CharField(max_length=20)
    course_option = models.CharField(max_length=20, choices=COURSE_OPTIONS)
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    interview_date = models.DateField()
    resume = models.FileField(upload_to='resumes/')
    video = models.FileField(upload_to='videos/')
    suggestions = models.TextField()

    def __str__(self):
        return f"{self.user_name}'s Interview Information"
