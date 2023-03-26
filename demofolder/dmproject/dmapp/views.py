from django.shortcuts import render
from . models import People


# Create your views here.
def demo(request):
    obj=People.objects.all()
    return render(request,"index.html",{'result':obj})
