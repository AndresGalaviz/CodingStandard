from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from app.models import Document
from app.forms import DocumentForm

from app.src import nsiqcppstyle
import sys
import os
import re

def index(request):
    return render(request, 'parallax.html')

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )

def input(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        #Dictionary for grading values based on rules
        grading = {
            'FileNamePascalCase': request.POST.get('filename'),
            'VariableNaming': request.POST.get('variables'), 
            'UseSpaceIndentation': request.POST.get('indentation'),
            'IndentBlocks': request.POST.get('indentation_blocks'),
            'CommentsForFunctions': request.POST.get('documentation'), 
            'FunctionNaming': request.POST.get('functions'),
            'InitialComments': request.POST.get('initial_comments')
        }
        
        if form.is_valid():
            for f in request.FILES.getlist('docfile'):
                #f name of thefile
                #f.read() contents of the file
                #f = re.search(r'^.{6}(.{9}).{9}(.{19})_(.+\.cpp)', str(f)).group(1)
                newdoc = Document(docfile = f)
                newdoc.save()
            # Redirect to the document list after POST
            response = nsiqcppstyle.main([
                'nsiqcppstyle.py', 
                '--output=csv', '-f', 
                'filefilter.txt', 
                'media/documents/' + newdoc.folder_string, 
                grading
            ])
            
            return response
    else:
        form = DocumentForm()  # A empty, unbound form

    return render(
            request, 
            'input.html',
            {'form': form}
        )

def loading(request):
    return render(request, 'loading.html')

def final(request):
    return render(request, 'final.html')