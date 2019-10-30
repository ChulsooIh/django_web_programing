from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text #DB에서 오브젝트 이름 대신 질문 내용으로 노출

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choice', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text  # DB에서 오브젝트 이름 대신 컨텐츠 내용으로 노출