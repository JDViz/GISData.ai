from django.urls import path, include
from . import views

app_name = 'risk_management'

urlpatterns = [
    path('questionnaire/<int:meeting_id>/', views.questionnaire_view, name='questionnaire_view'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
    path('dataview/', views.data_view, name='data_view'),
    path('dash1/', views.risk_management_dashboard, name='risk_management_dashboard'),
    # Add more paths as needed
]
