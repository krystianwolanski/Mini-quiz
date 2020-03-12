from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Question(models.Model):
    question_text = models.CharField(max_length=256, verbose_name=u'Question\'s text')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return "{content} - {published}".format(content=self.question_text, published=self.is_published)
    def get_next(self):
        question = Question.objects.filter(pk__gt=self.pk).order_by('pk').first()
        return question.pk
            

class Answer(models.Model):
    """
    Answer's Model, which is used as the answer in Question Model
    """
    text = models.CharField(max_length=128, verbose_name=u'Answer\'s text')
    is_valid = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Punkty(models.Model):
    pkt = models.IntegerField(default=0)
    