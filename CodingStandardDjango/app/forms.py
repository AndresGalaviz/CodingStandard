# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    filename = forms.CharField(
    	label = 'Nombre de archivo',
    	widget = forms.NumberInput(attrs = {'class': 'validate', 'id': 'filename'})
    )

    variables = forms.CharField(
    	label = 'Nombres de variables',
    	widget = forms.NumberInput(attrs = {'class': 'validate', 'id': 'variables'})
    )

    indentation = forms.CharField(
    	label = 'Indentación',
    	widget = forms.NumberInput(attrs = {'class': 'validate', 'id': 'indentation'})
    )

    documentation = forms.CharField(
    	label = 'Documentación',
    	widget = forms.NumberInput(attrs = {'class': 'validate', 'id': 'documentation'})
    )

    docfile = forms.FileField(
        label = 'Elija uno o más archivos',
        widget = forms.FileInput(attrs = {'accept': '.cpp', 'multiple': 'true'})
    )