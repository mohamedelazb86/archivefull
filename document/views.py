from django.shortcuts import render,redirect
from document.models import Document
from settings.models import Document_type
from datetime import date,datetime
from django.contrib import messages
from django.http import HttpResponseRedirect
from contractor.models import Contractor
from django.http import JsonResponse

def documents(request):
    documents=Document.objects.all()
    document_type=Document_type.objects.all()
    if request.method=='POST':
        documenttype=request.POST['document_type']
        date_from=request.POST['date_from']
        date_to=request.POST['date_to']

        if date_from:
            date_from = datetime.strptime(date_from, "%Y-%m-%d").date()
        else:
            date_from = date(2007, 1, 1)  # تعيين قيمة افتراضية لتاريخ البداية

        if date_to:
            date_to = datetime.strptime(date_to, "%Y-%m-%d").date()
        else:
            date_to = date.today()  # تعيين قيمة افتراضية لتاريخ النهاية

        if date_from > date_to:
            messages.error(request,'عفوا لابد أن يكون ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            documents=Document.objects.filter(date__range=(date_from,date_to),document_type=documenttype)
            
    context={
        'documents':documents,
        'document_type':document_type
    }
    return render(request,'document/document.html',context)

def add_document(request):
    documnet_type=Document_type.objects.all()
    context={
        'documnet_type':documnet_type
    }
    return render(request,'document/add_document.html',context)


def getcontractordata(request):
    code=request.GET.get('code')
    if code:
           try:
            contractor = Contractor.objects.get(code=code)
            data = {
                "name": contractor.name,
                'sector':contractor.sector.name,
                'project':contractor.project,
                'archive_code':contractor.archive_code,
                
                
                
            }
           except Contractor.DoesNotExist:
            data = {"name": "غير موجود",
                    'sector':'غير موجود',
                    'project':'غير موجود',
                    
                    'archive_code':'غير موجود',
                    
                    }
    else:
        data = {"name": "",
                'sector':'',
                'project':'',
                'archive_code':'',
                
                
                }
    
    return JsonResponse(data)


def add_document_all(request):
    if request.method=='POST':
        code=request.POST['code']
        try:
            contractor=Contractor.objects.get(code=code)
        except Contractor.DoesNotExist:
            messages.error(request,'عفوا هذا المقاول غير موجود')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        
        statment=request.POST['statment']
        date=request.POST['date']
        file=request.FILES.get('file_name')
        document_type=request.POST['document_type']
        notes=request.POST['notes']

        Document.objects.create(
            statment=statment,
            file=file,
            date=date,
            document_type_id=document_type,
            notes=notes,
            user=request.user,
            contractor_id=contractor.id

        )
        messages.success(request,'تم حفظ المستند بنجاح')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 