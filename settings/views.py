from django.shortcuts import render

def document_type(request):
    return render(request,'settings/document_type.html',{})

def sector(request):
    return render(request,'settings/sector.html',{})
