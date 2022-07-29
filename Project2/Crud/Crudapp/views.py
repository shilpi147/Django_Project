from django.http import HttpResponse
from django.shortcuts import render
from . models import Employee

# Create your views here

def Registration(request):
    return render(request,'Registration.html')

def Insert(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        

        if Employee.objects.filter(username=username).exists() and Employee.objects.filter(email=email).exists():
            return HttpResponse("Username / Email ID already exsists ! Please try another !")
        
        obj=Employee()
        obj.username=username
        obj.password=password
        obj.email=email
        obj.phone=phone
        obj.gender=gender
        obj.save()

        return render(request,'Insert.html')
    else:

        return render(request,'Registration.html')
def View(request):
    a=Employee.objects.all()
    context={'data':a}
    return render(request,'View.html',context)

def Update(request,id):
    res=Employee.objects.get(id=id)
    context={'data':res}
    return render(request,'Update.html',context)

def successUpdate(request):
    if(request.method=='POST'):

        res = Employee.objects.get(id = request.POST.get('id'))
        res.username=request.POST.get('username')
        res.email = request.POST.get('email')
        res.phone = request.POST.get('phone')
        res.save()

        return render(request,'successUpdate.html')
    else:
        return render(request,'Update.html')

def Delete(request,id):
    res = Employee.objects.get(id=id)
    context = {'data':res}
    return render(request,'Delete.html',context)

def successDelete(request):
    if(request.method=='POST'):

        res = Employee.objects.get(id = request.POST.get('id'))
        res.delete()
        return render(request,'successDelete.html')
    else:
        return render(request,'Delete.html')
