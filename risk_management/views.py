from django.shortcuts import render, get_object_or_404, redirect
from django.urls import resolve
from .models import Meeting, Response, Question
from .forms import QuestionnaireForm
from django.contrib import messages


# def questionnaire_view(request, meeting_id):
#     meeting = get_object_or_404(Meeting, id=meeting_id)
#     questions = meeting.questions.all().order_by('order')
#
#     # Fetch the current question from the session or start from the first question
#     current_question_id = request.session.get('current_question_id', questions.first().id)
#     question = get_object_or_404(Question, id=current_question_id)
#
#     if request.method == 'POST':
#         form = QuestionnaireForm(request.POST, question=question)
#         if form.is_valid():
#             answer = form.cleaned_data['answer']
#             Response.objects.create(
#                 question=question,
#                 answer=answer,
#                 meeting=meeting
#             )
#             # Set the next question based on the selected answer or reset if no next question
#             if answer and answer.next_question:
#                 request.session['current_question_id'] = answer.next_question.id
#                 return redirect('risk_management:questionnaire_view', meeting_id=meeting_id)
#             else:
#                 if 'current_question_id' in request.session:
#                     del request.session['current_question_id']
#                 return redirect('risk_management:thank_you')
#
#     else:
#         form = QuestionnaireForm(question=question)
#
#     return render(request, 'risk_management/questionnaire.html',
#                   {'form': form, 'meeting': meeting, 'question': question})

def questionnaire_view(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    questions = meeting.questions.all().order_by('order')

    # Fetch the question index from the session or start from the first question
    question_index = request.session.get('question_index', 0)

    if question_index >= len(questions):
        # If all questions have been answered, reset the question index and redirect to the thank you page
        del request.session['question_index']
        return redirect('risk_management:thank_you')

    question = questions[question_index]

    if request.method == 'POST':
        form = QuestionnaireForm(request.POST, question=question)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer:
                Response.objects.create(
                    question=question,
                    answer=answer,
                    meeting=meeting
                )
            # Increment the question index and save it to the session
            request.session['question_index'] = question_index + 1
            return redirect('risk_management:questionnaire_view', meeting_id=meeting_id)

    else:
        form = QuestionnaireForm(question=question)

    return render(request, 'risk_management/questionnaire.html',
                  {'form': form, 'meeting': meeting, 'question': question})


def thank_you_view(request):
    return render(request, 'risk_management/thank_you.html')
# def thank_you_view(request, questionnaire_url):
#     # Passing the questionnaire_url to the template
#     return render(request, 'risk_management/thank_you.html', {'questionnaire_url': questionnaire_url})
