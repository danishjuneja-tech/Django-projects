from django.shortcuts import render, HttpResponse
from .models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def follow(request):
    return render(request, 'follow.html')

def mentor(request):
    return render(request, 'mentor.html')

def success(request):
    return render(request, 'success.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        sign = request.FILES.get('sign')
        hear = request.POST.get('hear')

        contact = Contact(name=name, phone=phone, email=email, desc=desc, sign=sign, hear=hear)
        contact.save()
    return render(request, 'contact.html')

def show (request):
    posts = Contact.objects.all()
    return render(request, 'post.html', {'posts': posts})
