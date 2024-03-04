from django.shortcuts import render,HttpResponse,redirect
#from message_app.models import Msg         #OR # we use this when were not in same folder
from .models import Msg         #we use this because its in same folder


# Create your views here.

def testing(request):
    return HttpResponse("Linked successfuly")

def create(request):
    print("request is: ",request.method)
    if request.method=="POST":
        #access from data
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['Mobile']
        msg=request.POST['msg']
        #print(n,"-",mail,"-",mob,"-",msg)
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return redirect('/dashboard')
       # return HttpResponse("DATA Fetched")
    else:
        return render(request,'create.html')

def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
    #return HttpResponse("Data featched from database")


def delete(request,rid):
   # print("Id to be delete:",rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')
   # return HttpResponse("ID to be delete: "+rid)

def edit(request,rid):
    #print("Id to be edited: ",rid)
    if request.method=='POST':
        #update new data
        upname=request.POST['uname']
        upemail=request.POST['uemail']
        upmob=request.POST['Mobile']
        upmsg=request.POST['msg']
        m=Msg.objects.filter(id=rid)        #we use filter here because we want data in queryset
        m.update(name=upname,email=upemail,mobile=upmob,msg=upmsg)
        return redirect('/dashboard')
    else:
        #form with old data
        context={}
        m=Msg.objects.get(id=rid)  #instade of filter we use get because filter is giving us query set in list and get directly giving us object
       # print(m)                   #we are getting get method because in edit.html we will need to use for loop 
        context['data']=m
        return render(request,'edit.html',context)
    #return HttpResponse("id to be edited:"+rid)