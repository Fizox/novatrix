from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm


def home(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def pricing(request):
    return render(request, "pricing.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for contacting us! We'll get back to you within 24 hours."
            )
            return redirect("contact")
    else:
        form = ContactForm()
    
    return render(request, "contact.html", {"form": form})
