from django.urls import path
from . import views

urlpatterns = [
    path('questionnaire/<int:meeting_id>/', views.questionnaire_view, name='questionnaire_view'),
    # Add more paths as needed
]
