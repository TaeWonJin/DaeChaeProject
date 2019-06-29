from django.db import models

class Twice(models.Model):
    CHOICES=(
        ('KR','한국'),
        ('JP','일본'),
        ('TW','대만'),
    )
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    brith=models.DateTimeField()
    nationality=models.CharField(max_length=20,choices=CHOICES)
    position=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()
    def __str__(self):
        return self.title