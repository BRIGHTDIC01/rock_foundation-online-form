from django.shortcuts import render
from .forms import ApplicationForm
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()

            # Send confirmation email
            send_mail(
                subject="Application Received - Rock-F Academy",
                message=(
                    f"Dear {application.first_name},\n\n"
                    "Your admission application has been successfully received.\n"
                    "Our admissions team will review your submission and contact you shortly.\n\n"
                    "Thank you for choosing Rock-F Academy."
                ),
                from_email="admin@rockfacademy.com",
                recipient_list=[application.guardian_email],
                fail_silently=False,
            )

            return render(request, 'success.html')
    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {'form': form})