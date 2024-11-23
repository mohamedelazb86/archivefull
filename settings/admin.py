from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from settings.models import Document_type,Sector

class Document_typeAdmin(SummernoteModelAdmin):
    list_display=['code','name']
    search_fields=['name','notes']

    summernote_fields = ('notes',)


class SectorAdmin(SummernoteModelAdmin):
    list_display=['code','name']
    search_fields=['name','notes']

    summernote_fields = ('notes',)

admin.site.register(Document_type,Document_typeAdmin)
admin.site.register(Sector,SectorAdmin)
