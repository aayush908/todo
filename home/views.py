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

def remove(request , event_id=0):
    
    if event_id:
        event_to_removed = event.objects.get(id = event_id)
        event_to_removed.delete()
        
    return redirect("/")
    
    
def search(request):
    if request.method == "POST":
        data = request.POST.get('find')
        print(data)
        alldata = event.objects.filter(work__icontains = data )
        print(alldata)
    context = {"data":alldata }
    print(context)
    return render(request, "search.html" , context)

def edit(request , event_id=0 ):
    if event_id:
        event_to_edit= event.objects.get(id = event_id)
        if request.method == "POST":
        # Handle editing existing event
            work = request.POST.get('work')
            workdes = request.POST.get('workdes')
            date = request.POST.get('date')
            print(work)

            if work and workdes and date:
                event_to_edit.work = work
                event_to_edit.workdes = workdes
                event_to_edit.date = date
                event_to_edit.save()
            return redirect("/")
        else:
            return HttpResponse("Invalid form data. All fields are required.")
    return redirect("/")
    
