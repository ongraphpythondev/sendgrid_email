from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail


# Create your views here.
def index(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            to = email_form.cleaned_data['to']
            subject = email_form.cleaned_data['subject']
            body = email_form.cleaned_data['body']
            _from = email_form.cleaned_data['_from']
            send_mail(subject, body, _from, [to],
                      fail_silently=False)
        else:
            email_form = EmailForm()
    else:
        email_form = EmailForm()
    return render(request, 'emailapp/email_form.html', {'email_form': email_form})
