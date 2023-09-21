from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def blog(request):
    return render(request,'pages/blog.html')
def contact(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    
    return render(request,'pages/contact.html',{'form':fm})
def features(request):
    return render(request,'pages/features.html')
def resume(request):
    return render(request,'pages/resume.html')