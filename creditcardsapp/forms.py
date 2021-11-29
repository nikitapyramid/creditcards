from django import forms
from .models import CreditCards,HistoryCard



class CreditCardsForm(forms.ModelForm):

    class Meta:
        model = CreditCards
        fields = (
            'seria',
            'number',
            'data_vipusk',
            'data_okonchania',
            'data_ispolzovania',
            'summa',
            'statuscard',
        )
        widgets = {
            'seria': forms.TextInput,
            'number': forms.TextInput,
            'data_vipusk': forms.TextInput,
            'data_okonchania': forms.TextInput,
            'data_ispolzovania': forms.TextInput,
            'summa': forms.TextInput,
        }

class HistoryCardForm(forms.ModelForm):

    class Meta:
        model = HistoryCard
        fields = (
            'id_card',
            'who_buy',
            'what_buy',
            'price_tovar',
        )
        widgets = {
            'who_buy': forms.TextInput,
            'what_buy': forms.TextInput,
            'price_tovar': forms.TextInput,
        }
