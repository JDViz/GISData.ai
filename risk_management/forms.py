from django import forms
from .models import Response, Answer


# class ResponseForm(forms.ModelForm):
#     class Meta:
#         model = Response
#         fields = ['question', 'answer', 'meeting']
#
#     def __init__(self, *args, **kwargs):
#         self.meeting = kwargs.pop('meeting', None)
#         super(ResponseForm, self).__init__(*args, **kwargs)
#         if self.meeting:
#             self.fields['question'].queryset = self.meeting.questions.all()
#             # You may need to filter possible answers based on the chosen question.
#             # Consider using JavaScript for that.


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Response
        # fields = ['answer']
        fields = []

    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', None)
        super(QuestionnaireForm, self).__init__(*args, **kwargs)

        if questions:
            for question in questions:
                self.fields[f'question_{question.id}'] = forms.ModelChoiceField(
                    queryset=question.possible_answers.all(),
                    widget=forms.RadioSelect,
                    label=question.text,
                    required=True
                )
