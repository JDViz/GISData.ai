from django import forms
from .models import Response


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Response
        # fields = ['answer']
        fields = []

    # def __init__(self, *args, **kwargs):
    #     questions = kwargs.pop('questions', None)
    #     super(QuestionnaireForm, self).__init__(*args, **kwargs)
    #
    #     if questions:
    #         for question in questions:
    #             self.fields[f'question_{question.id}'] = forms.ModelChoiceField(
    #                 queryset=question.possible_answers.all(),
    #                 widget=forms.RadioSelect,
    #                 label=question.text,
    #                 required=False
    #             )

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['answer']

    answer = forms.ModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        required=False
    )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super().__init__(*args, **kwargs)
        if question:
            self.fields['answer'].queryset = question.possible_answers.all()
            self.fields['answer'].label = question.text

