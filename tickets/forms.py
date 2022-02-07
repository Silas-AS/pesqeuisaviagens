from unittest.util import _MAX_LENGTH
from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from tickets.travel_class import class_type


class TicketsForms(forms.Form):
    origin = forms.CharField(label='Origem', max_length=100)
    destiny = forms.CharField(label='Destino', max_length=100)
    departure_date = forms.DateField(label='Ida', widget=DatePicker())
    return_date = forms.DateField(label='Volta', widget=DatePicker())
    search_date =forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)
    class_type = forms.ChoiceField(label='Tipo da Classe', choices=class_type)
    information = forms.ChoiceField(label='Informações extras', widget=forms.Textarea(), required=False)
    email = forms.EmailField(label='Email', max_length=150)