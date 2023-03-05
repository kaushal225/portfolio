from django.shortcuts import render,redirect
from django.core.mail import send_mail,BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def home(request):
    return render(request,'portfolio/index.html')
def skills(request):
    return render(request,'portfolio/skills.html')
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if(form.is_valid()):
            subject="contact details"
            body={
                'first_name':form.cleaned_data['first_name'],
                'last_name':form.cleaned_data['last_name'],
                'phone_number':form.cleaned_data['contact_number'],
                'email_address':form.cleaned_data['email_address'],
                'message':form.cleaned_data['message']
            }
            message='\n'.join(body.values())
            try:
                send_mail(subject,message,body['email_address'],['kaushaltiwari8167@gmail.com'])
            except BadHeaderError:
                return HttpResponse('invalid header error')
            return redirect('home')
    form=ContactForm()
    return render(request,'portfolio/contact.html',{'form':form})