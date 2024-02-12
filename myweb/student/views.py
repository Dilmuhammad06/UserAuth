from django.shortcuts import render,redirect
from.models import IMages
from .forms import ImageForms

def index(request):
    images = IMages.objects.all()
    data = {
        'title':'ImageView',
        'images':images
    }
    
    return render(request, 'student/index.html', context=data)

def posting(request):
    if request.method == 'POST':
        form = ImageForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ImageForms()
    return render(request,'student/posting.html',{'form':form})