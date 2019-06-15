from django.db import models
from django.contrib.auth.models import User
# Create your models here.

LEVEL_CHOICES = (
    ('EA','Easy'),
    ('MI','Middle'),
    ('HI','High'),
)


class Sentence(models.Model):
    id = models.AutoField(primary_key=True)
    src = models.CharField(max_length=200, default="")
    kosub = models.CharField(max_length=200)
    ensub = models.CharField(max_length=200)

    def __str__(self):
        return "{0}: {1}".format(self.ensub, self.kosub)


class History(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Sentence, default=None, on_delete=models.CASCADE)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='MI')
