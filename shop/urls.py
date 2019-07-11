from django.urls import path
from .views import *



urlpatterns = [path('rubric/<int:rubric_id>/', by_rubric, name='by_rubric'),
                path("", index, name='index'),
               path('add/', BoardCreateView.as_view(), name="add")]