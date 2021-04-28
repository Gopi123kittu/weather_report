from django.urls import path

from . import views

app_name = 'reporting'

urlpatterns = [
    path('collect_data', views.getreport, name='getreport'),
    path('get_result', views.getresult, name='getresult'),
]