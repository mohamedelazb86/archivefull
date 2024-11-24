from django.db import models
from settings.models import Sector

class Contractor(models.Model):
    code=models.CharField(max_length=75)
    name=models.CharField(max_length=120)
    sector=models.ForeignKey(Sector,related_name='contractor_sector',on_delete=models.SET_NULL,null=True,blank=True)
    project=models.CharField(max_length=120)
    item=models.CharField(max_length=150)
    notes=models.TextField(max_length=1500)
    archive_code=models.CharField(max_length=75,null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.archive_code=self.sector.name + '_' +self.code
        super(Contractor,self).save(*args,**kwargs)
