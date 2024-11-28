from django.urls import path
from . import views

app_name='contractor'

urlpatterns = [
    path('',views.contractor,name='contractor'),
    path('add_contractor',views.add_contractor,name='add-contractor'),
    path('delete-contractor',views.delete_contractor,name='delete-contractor'),
    path('edit-contactor',views.edit_contractor,name='edit-contractor'),


    path('<int:id>',views.add_document,name='add-document'),
    path('add-document-contractor',views.add_document_contractor,name='add-document-contractor'),
    path('delete-document',views.delete_document_contractor,name='delete-document'),
]


