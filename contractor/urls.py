from django.urls import path
from . import views

app_name='contractor'

urlpatterns = [
    path('',views.contractor,name='contractor'),
    path('add_contractor',views.add_contractor,name='add-contractor'),
    path('delete-contractor',views.delete_contractor,name='delete-contractor'),
    path('edit-contactor',views.edit_contractor,name='edit-contractor'),
]


