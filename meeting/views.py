from django.shortcuts import render,get_object_or_404,redirect

from .models import Meeting,Room
from django.forms import modelform_factory

def detail(request,id): 
    meeting_det = get_object_or_404( Meeting,pk=id)
    return render(request, 'meeting/detail.html',{"meetings": meeting_det})

def rooms(request): 
    todas_rooms = Room.objects.all()
    return render(request, 'rooms/total_room.html',{"rooms": todas_rooms})

MeetingForm = modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method == 'POST':
        #form has benn submited,process data+
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, 'meeting/new.html',{"form": form})
