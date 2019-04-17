from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Event

# Create your views here.
class CalendarView(ListView):
    model = Event
    template_name = 'newsdiary/calendar.html'
    context_object_name = 'events'