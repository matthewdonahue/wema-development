from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('calendar/', views.Calendar.as_view(), name='calendar')
]

app_name='home'