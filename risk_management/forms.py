from django import forms
from .models import Response


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
            self.fields['answer'].queryset = question.possible_answers.all().order_by('order')
            self.fields['answer'].label = question.text

