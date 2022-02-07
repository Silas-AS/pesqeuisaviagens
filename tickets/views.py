from django.shortcuts import render
from tickets.forms import TicketsForms


def index(request):
    form = TicketsForms()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def review_consultation(request):
    if request.method == 'POST':
        form = TicketsForms(request.POST)
        context = {'form': form}
        return render(request, 'minha_consulta.html', context)