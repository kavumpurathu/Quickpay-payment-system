
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from django.db.models import Sum,Avg
from .models import recharge
from .models import complaints
from.models import spweb,serviceprovider,userregistration,offer,Payment,wallet
from datetime import datetime
from .filters import rechargeFilter
import stripe
from django.core.files.storage import FileSystemStorage

stripe.api_key =settings.STRIPE_SECRET_KEY

    
    
def home(request):
    return render(request, 'index.html')
      
def indexadmin(request):
    return render(request, 'indexadmin.html')    
def adminuserview(request): 
    i = userregistration.objects.filter(status="1")
    s = userregistration.objects.filter(status="0") 
    return render(request, 'adminuserview.html',{'i':i,'s':s}) 
def deleteuser(request,uname):
    d=userregistration.objects.get(email=uname)
    d.status = 0
    d.save()
    u=User.objects.get(username=uname)
    u.is_active = False
    u.save()
    return redirect('adminuserview')
def reactivateuser(request,uname):
    d=userregistration.objects.get(email=uname)
    d.status = 1
    d.save()
    u=User.objects.get(username=uname)
    u.is_active = True
    u.save()
    return redirect('adminuserview')    
  
def adminspview(request): 
    j = serviceprovider.objects.filter(status="1")
    k = serviceprovider.objects.filter(status="0")
    return render(request, 'adminspview.html',{'j':j,'k':k})
def deletesp(request,uname):
    dp=serviceprovider.objects.get(uname=uname)
    dp.status = 0
    dp.save()
    uu=User.objects.get(username=uname)
    uu.is_active = False
    uu.save()
    return redirect( 'adminspview')
def reactivatesp(request,uname):
    d=serviceprovider.objects.get(email=uname)
    d.status = 1
    d.save()
    u=User.objects.get(username=uname)
    u.is_active = True
    u.save()
    return redirect('adminspview')         
def admindth(request): 
    dh = recharge.objects.filter(category="dth")
    
    return render(request, 'admindth.html',{'dh':dh})
def adminmob(request): 
    mo = recharge.objects.filter(category="mobile")
    return render(request, 'adminmob.html',{'mo':mo})
def admincmpl(request): 
    cm = complaints.objects.filter(r_status="1")
    return render(request, 'admincmpl.html',{'cm':cm})
def deletecmpl(request,id):
    cc=complaints.objects.get(id=id)
    cc.r_status = 0
    cc.save()
    return redirect( 'admincmpl') 
         
def user_reg(request):
    return render(request, 'user_reg.html')
def logout(request):
    return render(request,'index.html')
def usetpwd(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['pswd1']
        pass2 = request.POST['pswd2']
        pass3 = request.POST['pswd3']
        user = auth.authenticate(username = uname, password = pass1)
        if user is not None:
            u = User.objects.get(username = uname)
            
        
            if pass2 == pass3:
                u.set_password(pass3)
                u.save()
                messages.info(request,'Your Password Changed ,Please Login')
                return render(request,'login.html')
            else:
                messages.info(request,'Password Missmatch...')
                return redirect('usetpwd')
           
        else:
            messages.info(request,'Invalid Password...')
            return redirect('change_password')

    else:
        return render(request,'usetpwd.html')

def usetpwd1(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['pswd1']
        pass2 = request.POST['pswd2']
        pass3 = request.POST['pswd3']
        user = auth.authenticate(username = uname, password = pass1)
        if user is not None:
            u = User.objects.get(username = uname)
            
        
            if pass2 == pass3:
                u.set_password(pass3)
                u.save()
                messages.info(request,'Your Password Changed ,Please Login')
                return render(request,'login.html')
            else:
                messages.info(request,'Password Missmatch...')
                return redirect('usetpwd')
           
        else:
            messages.info(request,'Invalid Password...')
            return redirect('usetpwd1')

    else:
        return render(request,'usetpwd1.html')

        

def logincheck(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']
        if userregistration.objects.filter(email=username).exists():
            usr=userregistration.objects.get(email=username)
            if usr.status == 1:
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
                messages.info(request,'Your account is deactivated')    
                return render(request, 'login.html')
        elif serviceprovider.objects.filter(uname=username).exists():
             sp=serviceprovider.objects.get(uname=username)
             if sp.status == 1:
                 user = auth.authenticate(username=username, password=password)
                 if user is not None:
                     auth.login(request, user) 
                     if User.objects.filter(last_name="serviceprovider",username=username).exists():
                        return render(request, 'sphome.html')
                     else:
                         return render(request,'userhome.html')
                 else:
                     messages.info(request, 'invalid username/password')
                     return render(request, 'login.html')
             else:
                 messages.info(request,'Your account is deactivated')    
                 return render(request, 'login.html')
        else: 
             user = auth.authenticate(username=username, password=password)
             if user is not None:
                auth.login(request, user)
                return redirect('indexadmin')
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
        rad = request.POST['type']
        if(rad=='wallet'):
            
            a=str(amount)
            aa=int(a)
            m=wallet.objects.all()
            Idlist=[]
            for e in m:
                Idlist.append(e.id)
            maxid=max(Idlist)   
            k=wallet.objects.get(id=maxid)
            am=k.c_bal
            amt=int(am)
            if(aa <= amt):
                nm=amt-aa
                # wl=wallet.objects.get(id=maxid)
                k.c_bal=nm
                k.save()
                dr = recharge(uname=uname,fname=fname,service_no=cno, s_provider=sprv,category="dth", amount=amount,date=datetime.now(),commision=int(amount)*30/100)
                dr.save()
                messages.success(request,'Your Rechage is Successfull.!!!!')
                return redirect( '/wallt')
            else:
                messages.success(request,'Not enough balance in your wallet, please add money to proceed.!!')
                return redirect( '/wallt')  
       
        # stat = request.POST['status']
        if(rad=='stripe'):
            dr= recharge(uname=uname,fname=fname,service_no=cno,s_provider=sprv,category="dth",amount=amount,date=datetime.now(),commision=int(amount)*30/100)
            dr.save()
            # messages.success(request,'Your Rechage is Successfull')
            return redirect('/rechargepay') 
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
        rad =request.POST['type']
        if(rad=='wallet'):
            a=str(amount)
            aa=int(a)
            m=wallet.objects.all()
            Idlist=[]
            for e in m:
                Idlist.append(e.id)
            maxid=max(Idlist)   
            k=wallet.objects.get(id=maxid)
            am=k.c_bal
            amt=int(am)
            if(aa <= amt):
                nm=amt-aa
                # wl=wallet.objects.get(id=maxid)
                k.c_bal=nm
                k.save()
                mob = recharge(uname=uname,fname=fname,service_no=mob, s_provider=sprv,category="mobile", amount=amount,date=datetime.now(),commision=int(amount)*30/100)
                mob.save()
                messages.success(request,'Your Rechage is Successfull.!!!!')
                return redirect( '/wallt')
            else:
                messages.success(request,'Not enough balance in your wallet, please add money to proceed.!!')
                return redirect( '/wallt')
        if(rad=='stripe'):
            mob = recharge(uname=uname,fname=fname,service_no=mob, s_provider=sprv,category="mobile", amount=amount,date=datetime.now(),commision=int(amount)*30/100)
            mob.save()
            
            return redirect( '/rechargepay')


def paynow(request):
    if request.method == 'POST':
        amt = request.POST['amount']
        cbal=request.POST['cbalance']
        a=str(amt)
        b=int(a)
        s=wallet.objects.get(c_bal=cbal)
        c=s.c_bal+b
        ss=wallet(c_bal=c,ad_money=b)
        ss.save()
      
        
        return redirect('rechargepaywal') 
        
def wallt(request):
    m=wallet.objects.all()
    Idlist=[]
    for e in m:
        Idlist.append(e.id)
    maxid=max(Idlist)      
    k=wallet.objects.filter(id=maxid)
    return render(request,'wallet.html',{'k':k})                                        
 

def payment(request):
    return render(request, 'payment.html')

def spdtls(request,spuname):
    sp=serviceprovider.objects.filter(uname=spuname)
    return render(request, 'spdtls.html',{'sp':sp})   
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
      




def sphome(request):
    return render(request, 'sphome.html')

def spregister(request):
    return render(request, 'spregister.html') 

def rehistory(request,uname):
   
    h = recharge.objects.filter(uname=uname)
    mfilter = rechargeFilter(request.GET,queryset=h)
    h=mfilter.qs
    return render(request, 'rehistory.html',{'h':h,'mfilter':mfilter}) 


def rerequest(request,suname,spname):
   
    com = recharge.objects.filter(s_provider=spname)
    myfilter = rechargeFilter(request.GET,queryset=com)
    com=myfilter.qs
    return render(request, 'rerequest.html',{'com': com,'myfilter':myfilter}) 
 

def userhome(request):
    return render(request, 'userhome.html')  
       

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
            usr=userregistration(fname=first_name,lname=last_name,mob=mob,email=email,status='1')
            usr.save()
            return render(request, 'index.html') 
        else: 
            messages.info(request,'Password Missmatch')
            return render(request, 'user_reg.html')
         
   else:
        return render(request, 'user_reg.html')    



def spsignup(request):
   if request.method == 'POST':
        res=request.FILES.get('pi1',True)
        if res==False:
            pass
        else:
            fs=FileSystemStorage()
            fs.save(res.name, res)
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
            sp=serviceprovider(uname=email,name=first_name,category=cate.lower(), website=website,mob=mob,email=email,status='1',img=res)
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
        newcat = request.POST['cat']
       
        sp = serviceprovider.objects.get(uname=suname)  
        sp.name = newname
        sp.save()
        sp.website = newweb
        sp.save()
        sp.mob = newmob
        sp.save()
        sp.category = newcat
        sp.save()
       
        
        messages.success(request,'Your profile is updated')
        return redirect('serviceprofile',suname)
    else:
        return render(request,'serviceprofile.html',suname)

def spreply(request,spname):
    cm = complaints.objects.filter(spname=spname)
    return render(request, 'addcomreply.html',{'cm': cm})




def vwoffer(request,spname,sname):
    ofr= offer.objects.filter(spname=spname,sname=sname)
    sp=serviceprovider.objects.filter(uname=spname)
    return render(request, 'vwoffer.html',{'ofr':ofr,'sp':sp}) 



def viewoffer(request):
    if request.method=='POST':
       val = request.POST['sl']
       ofr = offer.objects.filter(sname=val)
       sp=serviceprovider.objects.filter(name=val)
       return render(request,'vwoffer_user.html',{'ofr':ofr,'val':val,'sp':sp})

    else:
       return render(request,'mcharge.html')    


def viewoffer1(request):
    if request.method=='POST':
       val = request.POST['sl']
       ofr = offer.objects.filter(sname=val)
       sp=serviceprovider.objects.filter(name=val)
       return render(request,'vwoffer_user1.html',{'ofr':ofr,'val':val,'sp':sp})

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
    
        s = complaints.objects.get(id=id,spname=spname)  
        s.replay = rply
        s.save()
        s.status= sta
        s.save()
        messages.success(request,'Reply Added Successfully ')
        return redirect('newfun',id)
    else:
        return render(request,'addcomreply.html') 

def rechargepay(request):
    
            r=recharge.objects.all()
            Idlist=[]
            for e in r:
                Idlist.append(e.id)
            maxid=max(Idlist)   
            k=recharge.objects.filter(id=maxid)
            return render(request,'rechargepay.html',{'k':k})

def rechargepaywal(request):
   
            r=wallet.objects.all()
            Idlist=[]
            for e in r:
                Idlist.append(e.id)
            maxid=max(Idlist)   
            k=wallet.objects.filter(id=maxid)
            return render(request,'rechargepaywal.html',{'k':k}) 


def billfun(request,id,fname,s_provider,category,service_no,amount,date):
    template = get_template('invoice.html')
    context ={
    
        "invoice_id": id,
        "fname":fname,
        "s_provider":s_provider,
        "category":category,
        "service_no":service_no,
    #     "customer_name": "John Cooper",
        "amount": amount,
        "date":date,
    #     "today": "Today",
    }
    html = template.render(context)
    pdf = render_to_pdf('invoice.html',context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")       

def dthsum(request):  
    r=recharge.objects.filter(category="dth").aggregate(r1=Sum('commision')) 
    p=r['r1']
    return render (request,'admincommision.html',{'p':p}) 
def mobsum(request):  
    s=recharge.objects.filter(category="mobile").aggregate(r2=Sum('commision')) 
    q=s['r2']
    return render (request,'admincommision1.html',{'q':q})                  

                           
       
      
 

   
   




            

