from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Meeting, Response, Question, Answer
from .forms import QuestionnaireForm
import plotly.offline as pyo
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from . import dash_apps
import pandas as pd
# from django.contrib import messages


app = DjangoDash('RiskManagementDashboard')


def questionnaire_view(request, meeting_id):
    # Retrieve the Meeting instance based on the provided meeting_id or raise a 404 error if not found
    meeting = get_object_or_404(Meeting, id=meeting_id)
    # Fetch all the questions related to the meeting, ordered by the 'order' field
    questions = meeting.questions.all().order_by('order')

    # If the request is POST and contains 'reset' in its POST data
    if request.method == 'POST' and 'reset' in request.POST:
        # Remove the question_index from the session, essentially resetting the form's progress
        request.session.pop('question_index', None)
        # Redirect the user back to the questionnaire page to start from the beginning
        return redirect('risk_management:questionnaire_view', meeting_id=meeting_id)

    # Get the current progress (which question is being displayed) from the session, defaulting to 0 (first question)
    question_index = request.session.get('question_index', 0)

    # If the question index goes beyond the available questions
    if question_index >= len(questions):
        # Remove the question_index from the session since all questions have been answered
        del request.session['question_index']
        request.session.pop('latest_question', None)  # Remove latest_question if it exists
        request.session.pop('latest_answer', None)    # Remove latest_answer if it exists
        # Redirect the user to the thank you page
        return redirect('risk_management:thank_you')

    # Retrieve the current question based on the index
    question = questions[question_index]

    # Loop to handle conditional questions
    while question and question.conditional_answer:
        # Get the previous question if there is one
        prev_question = questions[question_index - 1] if question_index > 0 else None
        if prev_question:
            # Fetch the response to the previous question for this meeting
            prev_response = Response.objects.filter(meeting=meeting, question=prev_question).first()
            # If the response to the previous question matches the condition to show the current question
            if prev_response and prev_response.answer == question.conditional_answer:
                break
            else:
                # Otherwise, increment the question index to skip to the next question
                question_index += 1
                # Check if we have gone beyond the available questions
                if question_index >= len(questions):
                    question = None
                else:
                    question = questions[question_index]
        else:
            break

    # If there's no valid question left to be displayed
    if not question:
        # Remove the question_index from the session
        del request.session['question_index']
        request.session.pop('latest_question', None)  # Remove latest_question if it exists
        request.session.pop('latest_answer', None)    # Remove latest_answer if it exists
        # Redirect the user to the thank you page
        return redirect('risk_management:thank_you')

    # If the request is a POST request (meaning the form has been submitted)
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST, question=question)

        if form.is_valid():
            answer = form.cleaned_data['answer']
            # Create a new Response instance if an answer has been chosen
            if answer:
                Response.objects.create(
                    question=question,
                    answer=answer,
                    meeting=meeting
                )
                # Store the latest question and answer in session
                request.session['latest_question'] = question.text
                request.session['latest_answer'] = answer.text
            # Move on to the next question
            request.session['question_index'] = question_index + 1
            return redirect('risk_management:questionnaire_view', meeting_id=meeting_id)
    else:
        # If it's a GET request, instantiate the form for the current question
        form = QuestionnaireForm(question=question)

    # Render the questionnaire template, passing the form, meeting, and question to the context
    return render(request, 'risk_management/questionnaire.html',
                  {
                      'form': form,
                      'meeting': meeting,
                      'question': question,
                      'latest_question': request.session.get('latest_question'),
                      'latest_answer': request.session.get('latest_answer'),
                      'conditional': question.conditional_answer,
                  })


def thank_you_view(request):
    # Simply render the thank you page
    return render(request, 'risk_management/thank_you.html')


def data_view(request):
    # Your existing aggregate data
    aggregate_data = Response.objects.values('answer__text').annotate(count=Count('answer')).order_by('-count')

    # Extract data for existing plot
    answers = [item['answer__text'] for item in aggregate_data]
    counts = [item['count'] for item in aggregate_data]
    trace = go.Bar(x=answers, y=counts)
    layout = go.Layout(title='Overall Answers Distribution')
    fig = go.Figure(data=[trace], layout=layout)
    aggregate_plot_div = pyo.plot(fig, output_type='div', show_link=False)

    # Generate a plot for each question's responses
    questions = Question.objects.all()
    plots = []

    for question in questions:
        data = Response.objects.filter(question=question).values('answer__text').annotate(count=Count('answer'))

        # Extract data for plotting
        answers = [item['answer__text'] for item in data]
        counts = [item['count'] for item in data]

        trace = go.Bar(x=answers, y=counts)
        layout = go.Layout(title=f'Responses for: {question.text}')
        fig = go.Figure(data=[trace], layout=layout)

        plot_div = pyo.plot(fig, output_type='div', show_link=False)
        plots.append(plot_div)

    # Pass the generated plots to the template
    return render(request, 'risk_management/dataview.html', context={
        'aggregate_plot_div': aggregate_plot_div,
        'plots': plots,
        'questions': questions,
    })


def risk_management_dashboard(request):
    return render(request, 'risk_management/dashboard1.html')

