from django.urls import path, re_path

from .views import *

app_name = 'Fuel'
urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('change-status/', change_status, name='change_status'),
    path('agent-page/', agent_page, name='agent_page'),
    path('mission-complete/', mission_complete, name='mission-complete'),
    re_path(r'check-request-assigned/',
            check_request_assigned, name='check-request-assigned'),
    path('dashboard/', RequestFuelFormView.as_view(), name='dashboard'),
    re_path(r'check-agent-available/',
            check_fuel_request_assigned, name='check-agent-available'),
]
