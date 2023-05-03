from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def bengali(request):
    return render(request,'bengali.html')

def hindi(request):
    return render(request,'hindi.html')

def english(request):
    return render(request,'english.html')
