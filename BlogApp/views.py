from django.shortcuts import render, redirect
from . models import SiteConfig, ContactMessage 

# Create your views here.
def home(request):
    site_config = SiteConfig.objects.first()
    return render(request, 'blogapp/home.html', {'site_config': site_config})

def about(request):
    site_config = SiteConfig.objects.first()
    return render(request, 'blogapp/about.html', {'site_config': site_config})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('home')
    return render(request, 'blogapp/contact.html')

def privacy_policy(request):
    site_config = SiteConfig.objects.first()
    return render(request, 'blogapp/privacy_policy.html', {'site_config': site_config})
