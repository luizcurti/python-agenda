from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


# Create your views here.

def index(request):
    contatos = Contact.objects.order_by('-id').filter(
        visible=True
    )
    paginator = Paginator(contatos, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contacts/index.html', {
        'contatos': contatos
    })


def seeContact(request, contact_id):
    contato = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/seeContact.html', {
        'contato': contato
    })


def search(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Search term cannot be empty.'
        )
        return redirect('contacts:index')

    campos = Concat('first_name', Value(' '), 'last_name')

    contatos = Contact.objects.annotate(
        full_name=campos
    ).filter(
        Q(full_name__icontains=termo)
    )

    paginator = Paginator(contatos, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contacts/search.html', {
        'contatos': contatos
    })
