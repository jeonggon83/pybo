from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가
    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Serverstatus(models.Model):
    no = models.CharField(max_length=20, primary_key=True)
    server_id = models.TextField()
    temperature = models.CharField(max_length=5)
    humidity = models.TextField()
    reg_date = models.DateTimeField()
    tempAVG = models.CharField(max_length=5)
    humiAVG = models.CharField(max_length=5)

    def __str__(self):
        return self.no

class Company(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    company = models.CharField(max_length=40)
    last_update = models.DateField()

    def __str__(self):
        return self.company