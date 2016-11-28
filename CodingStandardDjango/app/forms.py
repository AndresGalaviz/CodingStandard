# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    filename = forms.CharField(
    	label = 'Nombre de archivo',
    	widget = fomrs.NumberInput(attrs = {'class': 'validate', 'id': 'filename'})
    )

    variables = froms.CharField(
    	label = 'Nombres de variables',
    	widget = fomrs.NumberInput(attrs = {'class': 'validate', 'id': 'variables'})
    )

    indentation = forms.CharField(
    	label = 'Indentación',
    	widget = fomrs.NumberInput(attrs = {'class': 'validate', 'id': 'indentation'})
    )

    documentation = forms.CharField(
    	label = 'Documentación',
    	widget = fomrs.NumberInput(attrs = {'class': 'validate', 'id': 'documentation'})
    )

    docfile = forms.FileField(
        label = 'Elija uno o más archivos'
    )