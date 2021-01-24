from django.shortcuts import render

# Create your views here.
#rander for HTML file call
from django.shortcuts import render
#HttpResponse For Response code
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request,'pages/home.html')
def noise(request):
    return render(request,'pages/denoising.html')
def super(request):
    return render(request,'pages/denoising2.html')

