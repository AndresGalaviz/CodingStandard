from __future__ import unicode_literals
import uuid
from django.db import models
import datetime

# Create your models here.
class Document(models.Model):
    folder_id = str(uuid.uuid1())
    foldername = 'documents/%Y%m%d' + folder_id
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    if len(month) == 1:
    	month = '0' + month
    day = str(now.day)
    if len(day) == 1:
    	day = '0' + day
    folder_string = year + month + day + folder_id
    docfile = models.FileField(upload_to = foldername)