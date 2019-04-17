from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class CalendarView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Event
    template_name = 'newsdiary/calendar.html'
    context_object_name = 'events'

    # def get_queryset(self):
    #     self.kwargs['pk']
    #     return Event.objects.filter(datetime__year=self.kwargs['pk'])

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'