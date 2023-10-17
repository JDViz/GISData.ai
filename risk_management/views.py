from django.shortcuts import render, get_object_or_404, redirect
from django.urls import resolve
from .models import Meeting, Response
from .forms import QuestionnaireForm
from django.contrib import messages


def questionnaire_view(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    questions = meeting.questions.all().order_by('order')

    if request.method == 'POST':
        form = QuestionnaireForm(request.POST, questions=questions)
        if form.is_valid():
            for question in questions:
                answer = form.cleaned_data[f'question_{question.id}']
                if answer is not None:
                    Response.objects.create(
                        question=question,
                        answer=answer,
                        meeting=meeting
                    )
            messages.success(request, 'Your responses have been recorded. Thank you!')
            return redirect('risk_management:thank_you')
            # questionnaire_url = reverse('risk_management:questionnaire', kwargs={'meeting_id': meeting_id})
            # questionnaire_url = resolve(request.path_info).url_name
            # return redirect('risk_management:thank_you', questionnaire_url=questionnaire_url)
    else:
        form = QuestionnaireForm(questions=questions)

    return render(request, 'risk_management/questionnaire.html', {'form': form, 'meeting': meeting})


# def questionnaire_view(request, meeting_id):
#     meeting = get_object_or_404(Meeting, id=meeting_id)
#
#     # Get the first unanswered question for the meeting.
#     unanswered_questions = meeting.questions.exclude(response__meeting=meeting).order_by('order')
#     if not unanswered_questions.exists():
#         messages.success(request, 'All questions have been answered. Thank you!')
#         return redirect('risk_management:thank_you')
#
#     question = unanswered_questions.first()
#
#     if request.method == 'POST':
#         form = QuestionnaireForm(request.POST, question=question)
#         if form.is_valid():
#             answer = form.cleaned_data['answer']
#             if answer:
#                 Response.objects.create(
#                     question=question,
#                     answer=answer,
#                     meeting=meeting
#                 )
#             return redirect('risk_management:questionnaire_view', meeting_id=meeting_id)
#
#     else:
#         form = QuestionnaireForm(question=question)
#
#     return render(request, 'risk_management/questionnaire.html',
#                   {'form': form, 'meeting': meeting, 'question': question})


def thank_you_view(request):
    return render(request, 'risk_management/thank_you.html')
# def thank_you_view(request, questionnaire_url):
#     # Passing the questionnaire_url to the template
#     return render(request, 'risk_management/thank_you.html', {'questionnaire_url': questionnaire_url})
