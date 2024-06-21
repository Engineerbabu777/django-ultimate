from django.shortcuts import render,redirect
from .form import ContactForm



# Create your views here.
def home_view(request):
    return render(request,'home.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            # form.save()
            return redirect('contact-success')
            # return render(request,'contact.html',{'form':ContactForm()})
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})


def contact_success_view(request):
    return render(request,'contact-success.html')