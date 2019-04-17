from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

now = datetime.datetime.now()

# Create your views here.
def temp(request):
    year = now.year
    month = now.month
    return redirect('/calendar/' + str(year) + str(month))

class CalendarView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = 'newsdiary/calendar.html'
    context_object_name = 'events'

    def get_queryset(self):
        if self.kwargs['pk'] >= 100000:
            year = self.kwargs['pk'] / 100
            month = self.kwargs['pk'] % 100
        else:
            year = self.kwargs['pk'] / 10
            month = self.kwargs['pk'] % 10
        return Event.objects.filter(datetime__year=year, datetime__month=month)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'