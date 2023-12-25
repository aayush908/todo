from django.shortcuts import render , HttpResponse, redirect
from home.models import event
# Create your views here.
def home(request , event_id=0):
    if request.method == "POST":
        work = request.POST["work"]
        workdes = request.POST["workdes"]
        date = request.POST["date"]
        event1 =event(work = work , workdes = workdes ,  date = date)
        event1.save()

    if event_id:
        event_to_removed = event.objects.get(id = event_id)
        event_to_removed.delete()
    allevent = event.objects.all()
    context = {'allevent' : allevent}
    
    return render(request,"home.html" , context)


