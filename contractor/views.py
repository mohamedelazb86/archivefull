from django.shortcuts import render,redirect
from django.contrib import messages
from contractor.models import Contractor
from settings.models import Sector,Document_type
from document.models import Document
from django.http import HttpResponseRedirect

def contractor(request):
    contractor=Contractor.objects.all()
    sector=Sector.objects.all()

    context={
        'contractor':contractor,
        'sector':sector
    }
    return render(request,'contractor/contractor.html',context)
def add_contractor(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        sector=request.POST['sector']
        project=request.POST['project']
        item=request.POST['item']
        notes=request.POST['notes']


        Contractor.objects.create(
            code=code,
            name=name,
            sector_id=sector,
            project=project,
            item=item,
            notes=notes
        )

        messages.success(request,'تم إضافة مقاول جديد بنجاح')
        return redirect('/contractor/')
    
def delete_contractor(request):
    if request.method=='POST':
        contractor_id=request.POST['id']
        contractor=Contractor.objects.get(id=contractor_id)
        contractor.delete()

        messages.success(request,'تم حذف مقاول بنجاح ')
        return redirect('/contractor/')
def edit_contractor(request):
    if request.method=='POST':
        contractor_id=request.POST['id']
        contractor=Contractor.objects.get(id=contractor_id)

        code=request.POST['code']
        name=request.POST['name']
        sector=request.POST['sector']
        project=request.POST['project']
        item=request.POST['item']
        notes=request.POST['notes']

        contractor.code=code
        contractor.name=name
        contractor.sector_id=sector
        contractor.project=project
        contractor.item=item
        contractor.notes=notes

        contractor.save()

        messages.success(request,'تم العتديل بنجاح')
        return redirect('/contractor/')

def add_document(request,id):
    contractor=Contractor.objects.get(id=id)
    documents=Document.objects.filter(contractor=contractor)

    contractors=Contractor.objects.all()
    document_type=Document_type.objects.all()

    context={
        'contractor':contractor,
        'documents':documents,
        'contractors':contractors,
        'document_type':document_type
        
    }

    return render(request,'contractor/add_document.html',context)

def add_document_contractor(request):
   
    if request.method=='POST':
        contractor_id=request.POST['id']
        contractor=Contractor.objects.get(id=contractor_id)
        statment=request.POST['statment']
        date=request.POST['date']
        document_type=request.POST['document_type']
        
        file=request.FILES.get('file_name')
        notes=' لايوجد'
        user=request.user

        Document.objects.create(
            statment=statment,
            date=date,
            document_type_id=document_type,
            contractor_id=contractor.id,
            file=file,
            notes=notes,
            user=user
        )
        messages.success(request,'تم إضافة مستند بنجاح')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def delete_document_contractor(request):
    if request.method=='POST':
        document_id=request.POST['id']
        document=Document.objects.get(id=document_id)
        document.delete()
        messages.success(request,'تم الحذف بنجاح')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        
        
