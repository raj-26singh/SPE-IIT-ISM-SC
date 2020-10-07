from django.shortcuts import render, get_object_or_404, redirect
from .models import Events, Registeration
from django.views.generic import ListView, DetailView
import datetime
from .forms import RegisterForm, SingleRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#     IMPORTANT ! ! !
#Positivly update EventListView's QuerySet by 2040!

def home(request):
    context = {
        'events': Events.objects.all()
    }
    return render(request, 'events/home.html', context)

class EventListView(ListView):
    model = Events
    template_name = 'events/home.html'
    context_object_name = 'events'
    order_by = ['-reg_date']
    paginate_by = 3

    def get_queryset(self):
        date_1=datetime.date.today()
        return Events.objects.filter(reg_date__lte=datetime.date(2040,1,1),
                                     reg_date__gte=date_1).order_by('-id')

class EventDetailView(DetailView):
    model = Events

class PastEventListView(ListView):
    model = Events
    template_name = 'events/home.html'
    context_object_name = 'events'
    order_by = ['-reg_date']
    paginate_by = 3

    def get_queryset(self):
        date_1=datetime.date.today()
        date_1=date_1 + datetime.timedelta(days=-1)
        return Events.objects.filter(reg_date__lte=date_1,
                                     reg_date__gte=datetime.date(2019,1,1)).order_by('-id')

@login_required
def TeamEventRegisterView(request):
    if request.method == 'POST':
        r_form = RegisterForm(request.POST,instance=request.user)

        if r_form.is_valid():
            r_form.save()
            messages.success(request, f'You have been registered for the event.')
            return redirect('/')

    else:
        r_form = RegisterForm(instance=request.user)

    context={
        'r_form': r_form
    }
    return render(request, 'events/registration_details.html', context)

@login_required
def EventRegisterView(request):
    if request.method == 'POST':
        single_form = SingleRegisterForm(request.POST,instance=request.user)

        if single_form.is_valid():
            single_form.save()
            messages.success(request, f'You have been registered for the event.')
            return redirect('/')

    else:
        single_form = SingleRegisterForm(instance=request.user)

    context={
        'r_form': single_form
    }
    return render(request, 'events/registration_details.html', context)