from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

#function-based view
def test_view(request):
    return render(request, "pages/test.html")

def about_view(request):
    return render(request, "pages/about.html")

def contact_view(request):
    if request.method == "POST":
        # send the message
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Sending email")

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            full_message = f"This is an email from your portfolio page\nName: {name}\nEmail: {email}\nMessage: {message}"

            send_mail(
                "Email from " + name,
                full_message,
                email,
                ["brett.byrd@sdgku.edu"]
            )
            print("Email sent")
        else:
            print("Invalid data on the form")
    else:
        form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})