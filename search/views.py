from django.shortcuts import render
from document.models import Document
from contractor.models import Contractor
from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from datetime import datetime,date
from settings.models import Sector


def search(request):
    documents=Document.objects.all()
    sectors=Sector.objects.all()
    if request.method=='POST':
        code=request.POST['code']
        try:

            contractor=Contractor.objects.get(code=code)
        except Contractor.DoesNotExist:
            messages.error(request,'عفوا المقاول غير مودود')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        date_from=request.POST['date_from']
        date_to=request.POST['date_to']

        sector=request.POST['sector']

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
        if sector=='all':
        
            documents=Document.objects.filter(date__range=(date_from,date_to),contractor=contractor)
        else:
            documents=Document.objects.filter(date__range=(date_from,date_to),contractor=contractor,sector=sector)
            





    context={
        'documents':documents,
        'sectors':sectors
    }
    return render(request,'search/search.html',context)

def getcontractordata(request):
    code=request.GET.get('code')
    if code:
           try:
            contractor = Contractor.objects.get(code=code)
            data = {
                "name": contractor.name,
                
                
                
                
            }
           except Contractor.DoesNotExist:
            data = {"name": "",
                  
                    
                    }
    else:
        data = {"name": "",
              
                
                
                }
    
    return JsonResponse(data)
