from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from.models import Contacts
from .forms import ContactsForm


def new_contacts(request):
    form = ContactsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("main"))
    context = {'form':form}
    return render(request, 'contacts/new_contacts.html', context=context)