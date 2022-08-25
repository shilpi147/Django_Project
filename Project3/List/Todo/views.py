from pickle import OBJ
from django.shortcuts import render
from . models import Information

# Create your views here.
def Welcome(request):
    return render(request,'Welcome.html')

def Create(request):
    return render(request,'Create.html')
   
def Save(request):
    if request.method=="POST":
        list=request.POST.get('list')
        title=request.POST.get('title')
        discription=request.POST.get('discription')
        date=request.POST.get('date')

        obj=Information()
        obj.list=list
        obj.title=title
        obj.discription=discription
        obj.date=date

        obj.save()
        return render(request,'Save.html')
    else:
        return render(request,'Welcome.html')

def Viewl(request):
    obj=Information.objects.all()
    context={'data':obj}
    return render(request,'Viewl.html',context)

def Edit(request,id):
    res=Information.objects.get(id=id)
    context={'data':res}
    return render(request,'Edit.html',context)

def successEdit(request):
    if(request.method=='POST'):
        res = Information.objects.get(id = request.POST.get('id'))
        res.list=request.POST.get('list')
        res.title = request.POST.get('title')
        res.discription = request.POST.get('discription')
        res.date = request.POST.get('date')
        res.save()

        return render(request,'successEdit.html')
    else:
        return render(request,'Edit.html')

def Delete(request,id):
    obj=Information.objects.get(id=id)
    context={'data':obj}
    return render(request,'Delete.html',context)

def successDelete(request):
    if request.method=='POST':
        res=Information.objects.get(id=request.POST.get('id'))
        res.delete()
        return render(request,'successDelete.html')
    else:
        return render(request,'Viewl.html')
    