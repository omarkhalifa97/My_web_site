from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return render(request,'index.html')
# Create your views here.
def submit(request):
    return HttpResponse('thanks')
