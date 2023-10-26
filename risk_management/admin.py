from django.contrib import admin
from .models import Answer, Question, Meeting, Response


class AnswerInline(admin.TabularInline):  # or use admin.StackedInline for a different visual presentation
    model = Question.possible_answers.through
    extra = 1  # number of empty forms presented
    readonly_fields = ('id',)
    ordering = ['answer__order', 'answer__text']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    # list_display = ['text', 'next_question']
    list_display = ['text', 'order']
    list_editable = ['order']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # list_display = ['text']
    list_display = ['text', 'order']
    list_editable = ['order']
    filter_horizontal = ('possible_answers',)


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ('questions',)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'meeting', 'timestamp']

    def timestamp(self, obj):
        return obj.timestamp
    timestamp.short_description = 'Timestamp UTC'
