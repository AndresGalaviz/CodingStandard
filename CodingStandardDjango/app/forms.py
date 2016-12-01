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

    indentation_blocks = forms.CharField(
        label = 'Bloques de Indentación',
        widget = forms.NumberInput(attrs = {'class': 'validate', 'id': 'indentation_blocks'})
    )

    documentation = forms.CharField(
    	label = 'Documentación',
    	widget = forms.NumberInput(attrs = {'class': 'validate', 'id': 'documentation'})
    )

    functions = forms.CharField(
        label = 'Nombres de funciones',
        widget = forms.NumberInput(attrs = {'class': 'validate', 'id': 'functions'})
    )

    intial_comments = forms.CharField(
        label = 'Comentarios iniciales',
        widget = forms.NumberInput(attrs = {'class': 'validate', 'id': 'initial_comments'})
    )

    docfile = forms.FileField(
        label = 'Elija uno o más archivos',
        widget = forms.FileInput(attrs = {'accept': '.cpp', 'multiple': 'true'})
    )