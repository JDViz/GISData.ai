from django.contrib import admin
from .models import Answer, Question, Meeting, Response


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text']
    filter_horizontal = ('possible_answers',)


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ('questions',)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'meeting', 'timestamp']
