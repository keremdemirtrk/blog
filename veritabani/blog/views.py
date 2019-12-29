from django.shortcuts import render
from .models import Post

# Create your views here.
posts = [
    {
        'author': 'Kerem Demirtürk',
        'title' :  'Mezun1',
        'content': 'First content',
        'date_posted': 'July 23,1998',
    },
    {
        'author': 'Kerim Demirtürk',
        'title' :  'Mezun2',
        'content': 'Second content',
        'date_posted': 'July 23,1998',
    },
]

def  home(request):
    context= {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def ilan(request):
    return render(request,'blog/ilan.html', {'title': 'Ilan'})

def cv(request):
    return render(request,'blog/cv.html', {'title': 'CV'})
