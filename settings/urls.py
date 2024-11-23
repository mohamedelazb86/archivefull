from django.urls import path
from . import views

app_name='settings'

urlpatterns = [
    path('document_type',views.document_type,name='document-type'),
    path('sector',views.sector,name='sector'),
]
