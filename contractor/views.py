from django.shortcuts import render,redirect
from django.contrib import messages
from contractor.models import Contractor
from settings.models import Sector

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

        
        
