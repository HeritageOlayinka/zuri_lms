from django.db import models

# Create your models here.


class Question(models.Model):
    # id  =  models.PrimaryKey(auto_increment=True)
    question_text = models.CharField(max_length = 255)
    question_description = models.CharField(max_length = 255, default = "Basic description")
    pub_note = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text



class Choices(models.Model):
    # id = models.PrimaryKey(auto_increment= True)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_answer =models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_answer
