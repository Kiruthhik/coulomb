from django.shortcuts import render
from .models import event
# Create your views here.
def home(request):
    return render(request,'index.html')

def events(request):
    events = event.objects.all()
    context = {'events':events}
    return render(request,'events.html',context)

def event_detail(request,id):
    event_detail = event.objects.get(id=id)
    context = {'event':event_detail}
    return render(request,'event.html',context)