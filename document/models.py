from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from settings.models import Document_type
from contractor.models import Contractor
import os
from django.utils.timezone import now

class Document(models.Model):
    statment=models.CharField(max_length=120)
    file=models.FileField(upload_to='files')
    date=models.DateField(default=timezone.now)
    document_type=models.ForeignKey(Document_type,related_name='document_type',on_delete=models.SET_NULL,null=True,blank=True)
    user=models.ForeignKey(User,related_name='document_user',on_delete=models.SET_NULL,null=True,blank=True)
    contractor=models.ForeignKey(Contractor,related_name='document_contractor',on_delete=models.CASCADE)
    notes=models.TextField(max_length=1500)

    def __str__(self):
        return self.statment
    
    def save(self, *args, **kwargs):
        if self.file:
            # Extract the file extension
            extension = os.path.splitext(self.file.name)[1]
            # Create a new file name
            new_filename = f"{self.contractor.code}_{now().strftime('%Y%m%d%H%M%S')}{extension}"
            # Set the new file name
            self.file.name = new_filename


        super().save(*args, **kwargs)

