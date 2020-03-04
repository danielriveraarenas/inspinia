from django import forms
from django_select2.forms import ModelSelect2Widget, Select2MultipleWidget
from .models import Colores, Marcas, Autos, Modelos


class AutosForm(forms.Form):
    marcas_id = forms.ModelChoiceField(queryset=Marcas.objects.all())
    modelo_id = forms.ModelChoiceField(queryset=Modelos.objects.all())
    colores = forms.ModelMultipleChoiceField(queryset=Colores.objects.all())
    precio = forms.IntegerField(
        label='Precio',
        widget=forms.NumberInput(
            attrs={'class': 'form-control'}
        ))
    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(
            attrs={'class': 'form-control'}),
    )
