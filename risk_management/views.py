from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting, Response, Question
from .forms import QuestionnaireForm
from django.contrib import messages


def questionnaire_view(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    questions = meeting.questions.all().order_by('order')

    # Check if the reset button was clicked
    if request.method == 'POST' and 'reset' in request.POST:
        request.session.pop('question_index', None)  # Remove the question_index from the session
        return redirect('risk_management:questionnaire_view', meeting_id=meeting_id)

    # Fetch the question index from the session or start from the first question
    question_index = request.session.get('question_index', 0)

    if question_index >= len(questions):
        # If all questions have been answered, reset the question index and redirect to the thank you page
        del request.session['question_index']
        return redirect('risk_management:thank_you')

    question = questions[question_index]

    while question and question.conditional_answer:
        prev_question = questions[question_index - 1] if question_index > 0 else None
        if prev_question:
            prev_response = Response.objects.filter(meeting=meeting, question=prev_question).first()
            if prev_response and prev_response.answer == question.conditional_answer:
                break
            else:
                question_index += 1
                if question_index >= len(questions):
                    question = None  # We've gone beyond the list of questions
                else:
                    question = questions[question_index]
        else:
            break

    if not question:
        # If we've exhausted all questions without finding a valid one, go to the thank you page
        del request.session['question_index']
        return redirect('risk_management:thank_you')

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
