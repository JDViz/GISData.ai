from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.CharField(max_length=255)
    possible_answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.text


class Meeting(models.Model):
    name = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.meeting.name} - {self.question.text} - {self.answer.text}"
