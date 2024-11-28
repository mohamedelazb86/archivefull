from django.shortcuts import render,redirect
from settings.models import Document_type,Sector
from django.contrib import messages
from document.models import Document
from django.db.models import Count

def document_type(request):
    document_type=Document_type.objects.all()

    context={
        'document_type':document_type
    }
    return render(request,'settings/document_type.html',context)
def add_document_type(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        Document_type.objects.create(
            code=code,
            name=name,
            notes=notes
        )
        messages.success(request,'تم إضافة نوع مستند بنجاح  ')
        return redirect('/document_type')
    
def delete_document_type(request):
    if request.method=='POST':
        document_type_id=request.POST['id']
        document_type=Document_type.objects.get(id=document_type_id)
        document_type.delete()

        messages.success(request,'تم حذف نوع المستند بنجاح')
        return redirect('/document_type')
def edit_document_type(request):
    if request.method=='POST':
        document_type_id=request.POST['id']
        document_type=Document_type.objects.get(id=document_type_id)

        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        document_type.code=code
        document_type.name=name
        document_type.notes=notes

        document_type.save()
        messages.success(request,'تم التعديل بنجاح ')
        return redirect('/document_type')



def sector(request):
    sector=Sector.objects.all()

    context={
        'sector':sector
    }
    return render(request,'settings/sector.html',context)

def add_sector(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        Sector.objects.create(
            code=code,
            name=name,
            notes=notes
        )
        messages.success(request,'تم إضافة نوع مستند بنجاح  ')
        return redirect('/sector')
    
def delete_sector(request):
    if request.method=='POST':
        sector_id=request.POST['id']
        sector=Sector.objects.get(id=sector_id)
        sector.delete()

        messages.success(request,'تم حذف نوع المستند بنجاح')
        return redirect('/sector')
    
def edit_sector(request):
    if request.method=='POST':
        sector_id=request.POST['id']
        sector=Sector.objects.get(id=sector_id)

        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        sector.code=code
        sector.name=name
        sector.notes=notes

        sector.save()
        messages.success(request,'تم التعديل بنجاح ')
        return redirect('/sector')
    
def dashbord(request):

    sector=Sector.objects.all().count()
        
    # Group orders by status and count them
    document_sector_counts = Document.objects.values('contractor__sector__name').annotate(count=Count('id'))

    # Prepare data for Chart.js
    sector_labels = [entry['contractor__sector__name'] for entry in document_sector_counts]
    sector_data = [entry['count'] for entry in document_sector_counts]

    context = {
        'sector_labels' : sector_labels,
        'sector_data' : sector_data,

        'sector':sector,
    }

    return render(request,'settings/dashbord.html',context)



