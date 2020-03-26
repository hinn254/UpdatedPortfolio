from django.shortcuts import render
from portfolio.forms import ContactForm
from django.core.mail import send_mail
# Create your views here.

def thanks(request):
    return render(request,"portfolio/thanks.html")


def index(request):
    name=''
    email=''
    comment=''


    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        message=form.cleaned_data.get("message")

        subject= "A Visitor's Message"


        comment= name + " with the email, " + email + ", sent the following message:\n\n" + message;
        send_mail(subject, comment, 'portfoliohinn@gmail.com', [email])

        return thanks(request)

    else:
        return render(request, "portfolio/index.html",{"form":form})
