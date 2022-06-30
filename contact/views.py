from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact form Submited!')
            return render(request, 'home/index.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
