from django.db.models import Q
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
from datetime import datetime, timedelta, time
import random

def index(request):
    '''facility = Facility.objects.all().order_by('-id')[:4]
    category = Category.objects.all()
    d = {'category': category,'facility': facility}'''
    return render(request, 'index.html')

def termsandcondition(request):
    return render(request, 'termsandcondition.html')

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'user_login.html',d)


def register(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fullname']
        mn = request.POST['mobilenumber']
        e = request.POST['email']
        p = request.POST['password']
        try:
            User.objects.create_user(username=e, password=p, first_name=f,last_name=mn)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'register.html',d)







def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'admin_login.html',d)

def Logout(request):
    logout(request)
    return redirect('index')



def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    usercount = User.objects.filter(is_staff=0).count()
    enquirycount = Enquiry.objects.all().count()
    mechaniccount = Mechanic.objects.all().count()
    servicecount = ServiceRequest.objects.all().count()
    nservicecount = ServiceRequest.objects.filter(adminstatus=None).count()
    rservicecount = ServiceRequest.objects.filter(adminstatus="Reject").count()
    cservicecount = ServiceRequest.objects.filter(adminstatus="Complete").count()
    d = {'newservice':newservice,'usercount':usercount,'enquirycount':enquirycount,'mechaniccount':mechaniccount,'servicecount':servicecount,'nservicecount': nservicecount,'rservicecount': rservicecount,'cservicecount': cservicecount}
    return render(request, 'admin_home.html',d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    servicecount = ServiceRequest.objects.filter(userid=request.user).count()
    nservicecount = ServiceRequest.objects.filter(adminstatus=None,userid=request.user.id).count()
    rservicecount = ServiceRequest.objects.filter(adminstatus="Reject",userid=request.user).count()
    cservicecount = ServiceRequest.objects.filter(adminstatus="Complete",userid=request.user).count()
    d = {'servicecount':servicecount,'nservicecount': nservicecount,'rservicecount': rservicecount,'cservicecount': cservicecount}
    return render(request, 'user_home.html',d)


def add_mechanic(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    if request.method=="POST":
        fn = request.POST['macname']
        mno = request.POST['mobilenumber']
        em = request.POST['email']
        ma = request.POST['macadd']
        try:
            Mechanic.objects.create(fullname=fn,mobileno=mno,emailid=em,address=ma)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'newservice':newservice}
    return render(request, 'add_mechanic.html', d)


def manage_mechanic(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    mechanic = Mechanic.objects.all()
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    d = {'mechanic':mechanic,'newservice':newservice}
    return render(request, 'manage_mechanic.html', d)

def delete_mechanic(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    mechanic = Mechanic.objects.get(id=pid)
    mechanic.delete()
    return redirect('manage_mechanic')


def edit_mechanic(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    mechanic = Mechanic.objects.get(id=pid)
    error = ""
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    if request.method == 'POST':
        fn = request.POST['macname']
        mno = request.POST['mobilenumber']
        em = request.POST['email']
        ma = request.POST['macadd']

        mechanic.fullname = fn
        mechanic.mobileno = mno
        mechanic.emailid = em
        mechanic.address = ma

        try:
            mechanic.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'mechanic':mechanic,'newservice':newservice}
    return render(request, 'edit_mechanic.html',d)



def add_category(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    if request.method=="POST":
        cn = request.POST['catename']

        try:
            Category.objects.create(categoryname=cn)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'newservice':newservice}
    return render(request, 'add_category.html', d)


def manage_category(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.all()
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    d = {'category':category,'newservice':newservice}
    return render(request, 'manage_category.html', d)

def delete_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.get(id=pid)
    category.delete()
    return redirect('manage_category')

def edit_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.get(id=pid)
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    error = ""
    if request.method == 'POST':
        cn = request.POST['catename']
        category.categoryname = cn
        try:
            category.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'category':category,'newservice':newservice}
    return render(request, 'edit_category.html',d)



def enquiry_form(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        fn = request.POST['enquirytype']
        mno = request.POST['description']
        em = request.POST['email']
        ma = request.POST['macadd']
        try:
            Enquiry.objects.create(fullname=fn,mobileno=mno,emailid=em,address=ma)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'enquiry_form.html', d)



def add_enquirytype(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    if request.method=="POST":
        en = request.POST['enqname']
        try:
            EnquiryType.objects.create(enqtypename=en)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'newservice':newservice}
    return render(request, 'add_enquirytype.html', d)


def view_enquirytype(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    enquirytype = EnquiryType.objects.all()
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    d = {'enquirytype':enquirytype,'newservice':newservice}
    return render(request, 'view_enquirytype.html', d)


def delete_enquirytype(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    enquirytype = EnquiryType.objects.get(id=pid)
    enquirytype.delete()
    return redirect('view_enquirytype')


def changepasswordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    error = ""
    if request.method=="POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        c = request.POST['confirmpassword']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error,'newservice':newservice}
    return render(request,'changepasswordadmin.html',d)


def changepassworduser(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        c = request.POST['confirmpassword']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'changepassworduser.html',d)




def enquiry_form(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    en=""
    enquirytypes = EnquiryType.objects.all()
    if request.method == 'POST':
        en = str(random.randint(10000000, 99999999))
        enquiryid = request.POST['enquirytype']
        des = request.POST['description']

        enquirytype = EnquiryType.objects.get(id=enquiryid)
        user = User.objects.get(id=request.user.id)
        try:
            Enquiry.objects.create(userid=user,enqno=en,enqtype=enquirytype,description=des,enqdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'en':en,'enquirytypes':enquirytypes}
    return render(request, 'enquiry_form.html',d)


def enquiry_history(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    enquiry = Enquiry.objects.filter(userid=request.user.id)
    d = {'enquiry':enquiry}
    return render(request, 'enquiry_history.html', d)


def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    user=User.objects.get(id=request.user.id)
    if request.method == 'POST':
        f = request.POST['fullname']
        m = request.POST['mobilenumber']

        user.first_name=f
        user.last_name=m
        try:
            user.save()
            error = "no"
        except:
            error="yes"
    d = {'error':error,'user':user}
    return render(request, 'user_profile.html',d)



def service_request(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    sn=""
    categorys = Category.objects.all()
    if request.method == 'POST':
        sn = str(random.randint(10000000, 99999999))
        categoryid = request.POST['category']
        vehname = request.POST['vehiclename']
        vehmodel = request.POST['vehiclemodel']
        vehbrand = request.POST['vehiclebrand']
        vehregno = request.POST['vehicleregno']
        serdate = request.POST['servicedate']
        sertime = request.POST['servicetime']
        deltype = request.POST['deltype']
        pickaddr = request.POST['pickupadd']

        cid = Category.objects.get(id=categoryid)
        user = User.objects.get(id=request.user.id)
        try:
            ServiceRequest.objects.create(userid=user,serviceno=sn,category=cid,vehiclename=vehname,vehiclemodel=vehmodel,vehiclebrand=vehbrand,vehicleregno=vehregno,servicedate=serdate,servicetime=sertime,deltype=deltype,pickupaddr=pickaddr,servicereqdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'sn':sn,'categorys':categorys}
    return render(request, 'service_request.html',d)


def service_history(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = ServiceRequest.objects.filter(userid=request.user.id)
    d = {'service':service}
    return render(request, 'service_history.html', d)


def reg_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user = User.objects.filter(is_staff=0)
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    d = {'user': user,'newservice':newservice}
    return render(request, 'reg_users.html',d)

def pending_service(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = ServiceRequest.objects.filter(adminstatus=None)
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    d = {'service': service,'newservice':newservice}
    return render(request, 'pending_service.html',d)

def rejected_services(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = ServiceRequest.objects.filter(adminstatus="Reject")
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    d = {'service': service,'newservice':newservice}
    return render(request, 'rejected_services.html',d)


def view_service_request(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = ServiceRequest.objects.get(id=pid)
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    error = ""
    if request.method == 'POST':
        adminstat = request.POST['status']
        service.adminstatus = adminstat
        try:
            service.save()
            error = "no"
        except:
            error = "yes"
    d = {'service': service,'error': error,'newservice':newservice}
    return render(request, 'view_service_request.html',d)


def pending_servicing(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = ServiceRequest.objects.filter(adminstatus="Accept")
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    d = {'service': service,'newservice':newservice}
    return render(request, 'pending_servicing.html',d)

def completed_service(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = ServiceRequest.objects.filter(adminstatus="Complete")
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    d = {'service': service,'newservice':newservice}
    return render(request, 'completed_service.html',d)


def view_service(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    mechanic = Mechanic.objects.all()
    service = ServiceRequest.objects.get(id=pid)
    try:
        total = int(service.partscharge) + int(service.servicecharge) + int(service.othercharge)
    except:
        total = 0
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    error = ""
    if request.method == 'POST':
        adminrem = request.POST['AdminRemark']
        serper = request.POST['serper']
        serchr = request.POST['servicecharge']
        partschr = request.POST['partcharge']
        addchr = request.POST['addcharge']
        adminstat = request.POST['status']
        mechanicid = Mechanic.objects.get(id=serper)
        service.adminremark = adminrem
        service.serviceby = mechanicid
        service.servicecharge = serchr
        service.partscharge = partschr
        service.othercharge = addchr
        service.adminstatus = adminstat
        service.adminremarkdate = date.today()
        try:
            service.save()
            error = "no"
        except:
            error = "yes"
    d = {'service': service,'error': error,'mechanic':mechanic,'total':total,'newservice':newservice}
    return render(request, 'view_service.html',d)


def respond_enquiry(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    enquiry = Enquiry.objects.filter(~Q(adminstatus=None))
    d = {'enquiry':enquiry,'newservice':newservice}
    return render(request, 'respond_enquiry.html', d)

def notrespond_enquiry(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    enquiry = Enquiry.objects.filter(adminstatus=None)
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    d = {'enquiry':enquiry,'newservice':newservice}
    return render(request, 'notrespond_enquiry.html', d)

def view_enquiry(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    enquiry = Enquiry.objects.get(id=pid)
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    if request.method == 'POST':
        adminres = request.POST['adminresponse']
        status = request.POST['status']
        enquiry.adminremarkdate = date.today()
        enquiry.adminresponse = adminres
        enquiry.adminstatus = status
        enquiry.save()
    d = {'enquiry':enquiry,'newservice':newservice}
    return render(request, 'view_enquiry.html', d)


def search_enquiry(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    enquirycount = 0
    enquiry=""
    sd=""
    click="no"
    if request.method == "POST":
        click="yes"
        sd = request.POST['searchdata']
        enquiry = Enquiry.objects.filter(enqno=sd)
        enquirycount = Enquiry.objects.filter(enqno=sd).count()
    d = {'enquiry':enquiry,'enquirycount':enquirycount,'sd':sd,'click':click,'newservice':newservice}
    return render(request,'search_enquiry.html',d)



def search_service(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    servicecount = 0
    service=""
    sd=""
    click="no"
    newservice = ServiceRequest.objects.filter(adminstatus=None)
    if request.method == "POST":
        click="yes"
        sd = request.POST['searchdata']
        service = ServiceRequest.objects.filter(serviceno=sd)
        servicecount = ServiceRequest.objects.filter(serviceno=sd).count()
    d = {'service':service,'servicecount':servicecount,'sd':sd,'click':click,'newservice':newservice}
    return render(request,'search_service.html',d)



def service_view(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    service = ServiceRequest.objects.get(id=pid)

    try:
        total = int(service.partscharge) + int(service.servicecharge) + int(service.othercharge)
    except:
        total = 0
    d = {'service': service,'total':total}
    return render(request, 'service_view.html',d)

def enquiry_view(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    enquiry = Enquiry.objects.get(id=pid)

    d = {'enquiry': enquiry}
    return render(request, 'enquiry_view.html',d)