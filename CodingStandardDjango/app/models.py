from __future__ import unicode_literals
import uuid
from django.db import models

# Create your models here.
class Document(models.Model):
    foldername = 'documents/%Y%m%d' + str(uuid.uuid4())
    docfile = models.FileField(upload_to = foldername)

