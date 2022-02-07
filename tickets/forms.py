from django import forms


class TicketsForms(forms.Form):
    origin = forms.CharField(label='Origem', max_length=100)
    destiny = forms.CharField(label='Destino', max_length=100)
    departure_date = forms.DateField(label='Ida')
    return_date = forms.DateField(label='Volta')