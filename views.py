from django.shortcuts import render,HttpResponse

# Create your views here.
def awal(request):
    return render(request, 'awal.html')

def home(request):
    return render(request, 'home.html')