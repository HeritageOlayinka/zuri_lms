from django.db import models

# Create your models here.


class Question(models.Model):
    # id  =  models.PrimaryKey(auto_increment=True)
    question_text = models.CharField(max_length = 255)
    pub_note = models.DateTimeField(auto_now_add=True)



class Choices(models.Model):
    # id = models.PrimaryKey(auto_increment= True)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_answer =models.CharField(max_length=20)
    votes = models.IntegerField(default=0)
