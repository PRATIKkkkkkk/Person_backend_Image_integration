from django.urls import path
from .views import PersonAPI, PersonDetailAPI

urlpatterns = [
    path('person/', PersonAPI.as_view()),
    path('person/<int:pk>/', PersonDetailAPI.as_view()),
]