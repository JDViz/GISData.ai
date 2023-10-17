from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.CharField(max_length=255)
    possible_answers = models.ManyToManyField(Answer)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['order']  # Add this line


class Meeting(models.Model):
    name = models.CharField(max_length=255)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp UTC")

    def __str__(self):
        return f"{self.meeting.name} - {self.question.text} - {self.answer.text}"
