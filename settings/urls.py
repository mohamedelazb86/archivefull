from django.urls import path
from . import views

app_name='settings'

urlpatterns = [
    path('document_type',views.document_type,name='document-type'),
    path('add_document_type',views.add_document_type,name='add-document-type'),
    path('delete_document_type',views.delete_document_type,name='delete-document-type'),
    path('edit_document_type',views.edit_document_type,name='edit-document-type'),

    # SECTOR
    path('sector',views.sector,name='sector'),
    path('add_sector',views.add_sector,name='add-sector'),
    path('delete_sector',views.delete_sector,name='delete-sector'),
    path('edit_sector',views.edit_sector,name='edit-sector'),

    #dashbord
    
]
