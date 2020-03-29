
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
#  from .models import mobrecharge
from .models import recharge
from .models import complaints
from.models import spweb,serviceprovider,userregistration,offer




# Create your views here.
def home(request):
    return render(request, 'index.html')

def user_reg(request):
    return render(request, 'user_reg.html')
def logout(request):
    return render(request,'index.html')      

def logincheck(request):

    if request.method == 'POST':
         username = request.POST['uname']
         password = request.POST['pswd']
         user = auth.authenticate(username=username, password=password)
         if user is not None:
             auth.login(request, user) 
             if User.objects.filter(last_name="serviceprovider",username=username).exists():
                 return render(request, 'sphome.html')   
             else:    
                 return render(request, 'userhome.html') 
   
         else:
             messages.info(request, 'invalid username/password')
             return render(request, 'login.html')
    else:
         return render(request, 'login.html')



def login(request):
    return render(request, 'login.html')
    
def services(request):
    return render(request, 'services.html')   

def aboutus(request):
    return render(request, 'aboutus.html') 

def comreply(request,uname):
    c=complaints.objects.filter(uname=uname)
    return render(request, 'comreply.html',{'c':c}) 

def vwcomplaints(request):
    return render(request, 'sphome.html')        

def care(request):
    sp= User.objects.filter(last_name="serviceprovider")
    return render(request, 'care.html',{'sp': sp})

def care1(request):
     if request.method == 'POST':
        uname = request.POST['uname']
        name = request.POST['name']
        compl = request.POST['ctype']  
        dtls = request.POST['details']
        sp = request.POST['sp']
        cmpls=complaints(uname=uname,spname=sp,name=name,complaint=compl,details=dtls,replay="null",status="Pending")
        cmpls.save()
        messages.success(request,'Complaint posted successfully ')
        sp= User.objects.filter(last_name="serviceprovider")
        return render(request, 'care.html',{'sp': sp})
           

def dcharge(request):
    srv = serviceprovider.objects.filter(category="dth")
    return render(request, 'dcharge.html',{'srv':srv}) 
def dcharge1(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        cno = request.POST['cardno']
        sprv = request.POST['sl']  
        amount = request.POST['amount']
        stat = request.POST['status']
        dr= recharge(uname=uname,fname=fname,service_no=cno, s_provider=sprv, amount=amount,status=stat,date=datetime.now())
        dr.save()
        messages.success(request,'Your Rechage is Successfull')
        return render(request, 'userhome.html') 
  



def mcharge(request):
    srv = serviceprovider.objects.filter(category="mobile")
    return render(request, 'mcharge.html', {'srv':srv}) 
def mcharge1(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        mob = request.POST['mob']
        sprv = request.POST['sl']  
        amount = request.POST['amount']
        stat = request.POST['status']
        mob = recharge(uname=uname,fname=fname,service_no=mob, s_provider=sprv, amount=amount,status=stat,date=datetime.now())
        mob.save()
        messages.success(request,'Your Rechage is Successfull')
        return render(request, 'userhome.html')


def payment(request):
    return render(request, 'payment.html')

def spdtls(request):
     return render(request, 'spdtls.html')   
def ofrsave(request):
    if request.method == 'POST':
        ofr = request.POST['ofr']
        suname = request.POST['uname']
        name = request.POST['name']
        dtls = offer(ofr_dtls=ofr,spname=suname,sname=name)
        dtls.save()
        messages.success(request,'Offer added successfully ')
        return render(request, 'spdtls.html') 
def delete(request,id):
    offr=offer.objects.get(id=id) 
    offr.delete()
    messages.success(request,'Deleted successfully ')
    return redirect('/vwoffer1')  

def vwoffer1(request):
     return render(request, 'spdtls.html')        
      


def paynow(request):
    return render(request, 'paynow.html') 

def sphome(request):
    return render(request, 'sphome.html')

def spregister(request):
    return render(request, 'spregister.html') 

def rehistory(request,uname):
    h = recharge.objects.filter(uname=uname)
    return render(request, 'rehistory.html',{'h':h}) 


def rerequest(request,suname,spname):
    com = recharge.objects.filter(s_provider=spname)
    return render(request, 'rerequest.html',{'com': com}) 

   

def userhome(request):
    return render(request, 'userhome.html')  

def wallet(request):
    return render(request, 'wallet.html') 

#def editprofile(request):
    #srv = serviceprovider.objects.filter(name=first_name,website=website,mob=mob,email=email)
    #return render(request, 'serviceprofile.html')          

def signup(request):
   if request.method == 'POST':
        first_name = request.POST['fname']
        last_name =request.POST['lname']
        mob=request.POST['mob']
        email = request.POST['email']
        uname = request.POST['email']
        pswd1= request.POST['pswd1']
        pswd2 = request.POST['pswd2']
        if(pswd1 == pswd2):
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already exist')
                return render(request, 'user_reg.html') 
            user = User.objects.create_user(username=uname, password=pswd1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            usr=userregistration(fname=first_name,lname=last_name,mob=mob,email=email)
            usr.save()
            return render(request, 'index.html') 
        else: 
            messages.info(request,'Password Missmatch')
            return render(request, 'user_reg.html')
         
   else:
        return render(request, 'user_reg.html')    



def spsignup(request):
   if request.method == 'POST':
        first_name = request.POST['name']
        cate=request.POST['cate']
        website=request.POST['web']
        mob=request.POST['mob']
        email = request.POST['email']
        uname = request.POST['email']
        pswd1= request.POST['pswd1']
        pswd2 = request.POST['pswd2']
        if(pswd1 == pswd2):
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already exist')
                return render(request, 'spregister.html') 
            user = User.objects.create_user(username=uname, password=pswd1, email=email, first_name=first_name, last_name="serviceprovider")
            user.save()
            sp=serviceprovider(uname=email,name=first_name,category=cate.lower(), website=website,mob=mob,email=email)
            sp.save()
            return render(request, 'index.html') 
        else:
            messages.info(request,'Password Missmatch')
            return render(request, 'spregister.html')
         
   else:
        return render(request, 'spregister.html')   

def serviceprofile(request,spuname):
    sp = serviceprovider.objects.filter(uname=spuname)
    return render(request, 'serviceprofile.html',{'sp':sp})           

def spsave(request,suname):
    if request.method == 'POST':
        newname = request.POST['name']
        newweb = request.POST['web']
        newmob = request.POST['mob']
        newemail = request.POST['email']

        sp = serviceprovider.objects.get(uname=suname)  
        sp.name = newname
        sp.save()
        sp.website = newweb
        sp.save()
        sp.mob = newmob
        sp.save()
        sp.email = newemail
        sp.save()
        messages.success(request,'Your profile is updated')
        return redirect('serviceprofile',suname)
    else:
        return render(request,'serviceprofile.html',suname)

# def reply(request,spuname,spname):
#     #com = serviceprovider.object.filter(uname=spuname,name=spname)
#     com = complaints.objects.filter(spname=spname)
#     return render(request, 'addcomreply.html',{'com': com})
def spreply(request,spname):
    cm = complaints.objects.filter(spname=spname)
    return render(request, 'addcomreply.html',{'cm': cm})




def vwoffer(request,spname,sname):
    ofr= offer.objects.filter(spname=spname,sname=sname)
    return render(request, 'vwoffer.html',{'ofr':ofr}) 


# def viewoffer(request,val):
#     ofr = offer.objects.filter(sname=val)
#     return render(request,'vwoffer_user.html',{'ofr':ofr})



def viewoffer(request):
    if request.method=='POST':
       val = request.POST['sl']
       ofr = offer.objects.filter(sname=val)
       return render(request,'vwoffer_user.html',{'ofr':ofr,'val':val})

    else:
       return render(request,'mcharge.html')    


def viewoffer1(request):
    if request.method=='POST':
       val = request.POST['sl']
       ofr = offer.objects.filter(sname=val)
       return render(request,'vwoffer_user1.html',{'ofr':ofr,'val':val})

    else:
       return render(request,'dcharge.html')  
      
   

def mobofr(request,sname):
     mf=offer.objects.filter(sname=sname)
     return render(request,'vwoffer_user.html',{'mf':mf})

def vwoffer_user(request,sp):
    s=recharge.objects.filter(s_provider=sp)
    return render(request,'vwoffer_user.html',{'s':s})



def complaintvw(request):
    return render(request, 'complaintvw.html')

def comview(request,spname):
    co = complaints.objects.filter(spname=spname)
    return render(request, 'complaintvw.html',{'co': co})    

def newfun(request,id):
    s=complaints.objects.get(id=id)
    return render(request, 'addcomreply.html',{'s': s})  

def complaintsave(request,id,spname):
    if request.method == 'POST':
        rply = request.POST['reply']
        sta =request.POST['status']
        # id = request.POST['id']
        # un = request.POST['uname']
        # spname= request.POST['spname']
        
        s = complaints.objects.get(id=id,spname=spname)  
        s.replay = rply
        s.save()
        s.status= sta
        s.save()
        messages.success(request,'Reply Added Successfully ')
        return redirect('newfun',id)
    else:
        return render(request,'addcomreply.html')     
       
       
 

   
   




            

