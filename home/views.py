from django.shortcuts import render , HttpResponse,render

# Create your views here.
def home(request):
    return render(request , "index.html")