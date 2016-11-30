from __future__ import unicode_literals
import uuid
from django.db import models
import datetime

# Create your models here.
class Document(models.Model):
    folder_id = str(uuid.uuid4())
    foldername = 'documents/%Y%m%d' + folder_id
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    folder_string = 'documents/' + year + month + day + folder_id
    docfile = models.FileField(upload_to = foldername)