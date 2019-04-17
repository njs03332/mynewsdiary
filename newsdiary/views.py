from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from calendar import monthrange

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
        return Event.objects.filter(datetime__year=self.year(), datetime__month=self.month())

    def day_events(self):
        day_events = [[]]
        events = self.get_queryset()
        for i in range(1,monthrange(self.year(), self.month())[1]+1):
            v = []
            for e in events.filter(datetime__day=i):
                v.append(e)
            day_events.append(v)
        return day_events

    def month(self):
        if self.kwargs['pk'] >= 100000:
            return int(self.kwargs['pk'] % 100)
        else:
            return int(self.kwargs['pk'] % 10)

    def year(self):
        if self.kwargs['pk'] >= 100000:
            return int(self.kwargs['pk'] / 100)
        else:
            return int(self.kwargs['pk'] / 10)

    def days(self):
        if self.kwargs['pk'] >= 100000:
            year = int(self.kwargs['pk'] / 100)
            month = int(self.kwargs['pk'] % 100)
        else:
            year = int(self.kwargs['pk'] / 10)
            month = int(self.kwargs['pk'] % 10)
        return range(1,monthrange(year, month)[1]+1)
    
    def before(self):
        return int(str(self.year()) + str(self.month()-1))

    def after(self):
        return int(str(self.year()) + str(self.month()+1))

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in another context variable
    #     if self.kwargs['pk'] >= 100000:
    #         year = int(self.kwargs['pk'] / 100)
    #         month = int(self.kwargs['pk'] % 100)
    #     else:
    #         year = int(self.kwargs['pk'] / 10)
    #         month = int(self.kwargs['pk'] % 10)
    #     context['days'] = monthrange(year, month)[1]
    #     context['month'] = month
    #     context['year'] = year
    #     return context

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'