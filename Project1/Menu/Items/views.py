from django.shortcuts import render
import random 
import string 

# Create your views here.

def order(request):
    a=string.ascii_letters
    l=[]
    for i in a:
        l.append(i)
    x=random.randint(5,7)
    b=random.sample(l,x)
    s= ""
    for i in b:
        s=s+i
    context = {'data':s}
    return render(request,'order.html',context)
