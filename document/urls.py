from django.urls import path
from . import views

app_name='document'

urlpatterns = [
    path('',views.documents,name='documents'),
    path('add-document',views.add_document,name='add-document'),
    path('get-contractor-data',views.getcontractordata,name='get-contractor-data'),

    path('add-document-all',views.add_document_all,name='add-document-all'),
    
]
