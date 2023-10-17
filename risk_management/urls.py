from django.urls import path
from . import views

app_name = 'risk_management'

urlpatterns = [
    path('questionnaire/<int:meeting_id>/', views.questionnaire_view, name='questionnaire_view'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
    # Add more paths as needed
]
