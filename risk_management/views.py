from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Response
from .forms import QuestionnaireForm
from django.contrib import messages


def questionnaire_view(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    questions = meeting.questions.all()

    if request.method == 'POST':
        form = QuestionnaireForm(request.POST, questions=questions)
        if form.is_valid():
            for question in questions:
                Response.objects.create(
                    question=question,
                    answer=form.cleaned_data[f'question_{question.id}'],
                    meeting=meeting
                )
            messages.success(request, 'Your responses have been recorded. Thank you!')
            return redirect('name_of_some_view')
    else:
        form = QuestionnaireForm(questions=questions)

    return render(request, 'risk_management/questionnaire.html', {'form': form, 'meeting': meeting})
