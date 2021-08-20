from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, 'resumes/home.html')

def experience(request):
    return render(request, 'resumes/experience.html')

def educational_history(request):
    return render(request, 'resumes/history.html')

def skills(request):
    return render(request, 'resumes/skills.html')

def hobbies(request):
    return render(request, 'resumes/hobbies.html')

def contact(request):

    if request.method == "POST":

        
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            
            messages.success(request, "Your Message has been submitted, thank you for your time")
            return redirect('index')

    else:
        form = ContactForm() 

    

    return render(request, 'resumes/contact.html', {'form':form}) 