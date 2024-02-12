from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages, auth
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return render(request, 'index.html')

def userregister(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        mob = request.POST['phone']
        password = request.POST['password']
        address = request.POST['address']
        img = request.FILES['img']
        wage=request.POST['wage']
        age=request.POST['age']
        if User1.objects.filter(email=email).exists():
            messages.info(request, "email already exists")
        else:
            user = Login.objects.create_user(
                username=email, password=password, usertype='user', ViewPassword=password, is_active=0)
            user.save()
            register = User1.objects.create(
                name=name, email=email, img=img, phone=mob, age=age, user=user, address=address, wages=wage)
            register.save()
            messages.info(request, "registration successfull")
            return redirect("/login")

    return render(request, 'user/user_register.html')

def workerregister(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        wage=request.POST['wages']
        address=request.POST['address']
        wtype=request.POST['wtype']
        img=request.FILES['img']
        idprof=request.FILES['img']
        password=request.POST['password']
        if Worker.objects.filter(email=email).exists():
            messages.info(request,"email already exists")
        else:
            worker=Login.objects.create_user(username=email, password=password, usertype='worker', ViewPassword=password, is_active=0)
            worker.save()
            register=Worker.objects.create(name=name, email=email, phone=phone, worker=worker, wages=wage, address=address, wtype=wtype, img=img, idprof=idprof)
            register.save()
            messages.info(request,"registration successfull")
            return redirect('/login')
        
    return render(request, 'worker/worker_register.html')

def contractorregister(request):
    if request.POST:
        qualification = request.POST['qualification']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
      
        img=request.FILES['img']
        idprof=request.FILES['img']
        password=request.POST['password']
        if Worker.objects.filter(email=email).exists():
            messages.info(request,"email already exists")
        else:
            contractor=Login.objects.create_user(username=email, usertype='contractor', password=password, ViewPassword=password, is_active=0)
            contractor.save()
            register=Contractor.objects.create(name=name, email=email, qualification=qualification, phone=phone, constructor=contractor, address=address, img=img, idprof=idprof)
            register.save()
            messages.info(request,"registration successfull")
            return redirect('/login')
        
    return render(request, 'contractor/contractor_register.html')


def login(request):
    if request.POST:

        email = request.POST["email"]
        password = request.POST["password"]
        # print(email, password,"test")
        user = authenticate(username=email, password=password)
        # print("trxdetxtrx",user)
        if user is not None:
            if user.usertype == "admin":
                messages.info(request, "welocme to  page admin")
                return redirect('/admin1')

            elif user.usertype == "user":
                print(user.usertype)
                request.session['uid'] = user.id
                messages.info(request, "welcome to user page")
                return redirect('/userhome')
            elif user.usertype == "contractor":
                print(user.usertype)
                request.session['uid'] = user.id
                messages.info(request, "welcome to contractor page")
                return redirect('/contractorhome')
            elif user.usertype == "worker":
                request.session['uid'] = user.id
                messages.info(request, "welcome to worker page")
                print(user.usertype)
                return redirect('/workerhome')
            else:
                messages.info(request, "invalid login")
        else:
            # messages.info(request, "User Not Approved")
            print("Type Not Get")
    return render(request,'login.html')

def contractorhome(request):
    return render(request, "contractor/contractorhome.html")


def workerhome(request):
    return render(request, "worker/workerhome.html")


def admin1(request):
    return render(request, "admin/adminhome.html")

def userhome(request):
    return render(request, "user/userhome.html")

def userviewcontractor(request):
    contract=Contractor.objects.all()
    return render(request, "user/viewcontractor.html",{'contract':contract})

def userviewprofile(request):
    uid=request.session['uid']
    update=User1.objects.filter(user=uid)
    if request.POST:
        if 'img' in request.FILES:
            img=request.FILES['img']
        else:
            img=update[0].img
        name = request.POST.get("Uname")
        img = request.FILES["img"]
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        wages=request.POST.get("wage")
        age=request.POST.get("age")

        updatedata = User1.objects.get(user=uid)
        updatedata.img=img
        updatedata.age=age
        updatedata.address=address
        updatedata.name=name
        updatedata.email=email
        updatedata.phone=phone
        updatedata.wages=wages
        updatedata.save()
        messages.info(request,"User updated successfuly")
        # uid=request.session['uid']
        # use=User1.objects.filter(user=uid)
    return render(request, "user/viewprofile.html",{'update':update})
def workerviewprofile(request):
    uid=request.session['uid']
    update=Worker.objects.filter(worker=uid)
    if request.POST:
        if 'img' in request.FILES and 'img1' in request.FILES:
            img=request.FILES['img']
            idprof=request.FILES['img1']
        else:
            img=update[0].img
            idprof=update[0].idprof
        name = request.POST.get("Wname")
        img = request.FILES["img"]
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        wages=request.POST.get("wage")
        age=request.POST.get("age")
        idprof=request.FILES["img1"]
        wtype=request.POST.get("wtype")
        

        updatedata = Worker.objects.get(worker=uid)
        updatedata.img = img
        updatedata.age=age
        updatedata.address=address
        updatedata.name=name
        updatedata.email=email
        updatedata.phone=phone
        updatedata.wages=wages
        updatedata.idprof=idprof
        updatedata.wtype=wtype
        updatedata.save()
        messages.info(request,"User updated successfuly")
        # uid=request.session['uid']
        # use=User1.objects.filter(user=uid)
    return render(request, "worker/viewprofile.html",{'update':update})
    
def contractorviewprofile(request):
    uid=request.session['uid']
    update=Contractor.objects.filter(worker=uid)
    if request.POST:
        if 'img' in request.FILES and 'img1' in request.FILES:
            img=request.FILES['img']
            idprof=request.FILES['img1']
        else:
            img=update[0].img
            idprof=update[0].idprof
        name = request.POST.get("Wname")
        img = request.FILES["img"]
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        qualification=request.POST.get("qualification")
        idprof=request.FILES["img1"]
       
        

        updatedata = Contractor.objects.get(worker=uid)
        updatedata.img = img
        updatedata.address=address
        updatedata.name=name
        updatedata.email=email
        updatedata.phone=phone
        updatedata.qualification=qualification
        updatedata.idprof=idprof
        updatedata.save()
        messages.info(request,"contractor updated successfuly")
        # uid=request.session['uid']
        # use=User1.objects.filter(user=uid)
    return render(request, "contractor/viewprofile.html",{'update':update})
   
   
def adminviewcontractor(request):
    contact=Contractor.objects.all()
    return render(request,'admin/viewcontractor.html',{'contact':contact})


def actioncontractor(request):
    status=request.GET['status']
    id=request.GET['id']
    print("#########################################################")
    print(id,status)
    contract=Login.objects.get(id=id)
    contract.is_active=int(status)
    contract.save()
    if status == "1":
        messages.info(request,"approved successfully")
    else:
        messages.info(request,"rejected your request")
    return redirect('/adminviewcontractor')

def delete(request):
    a=Userworkrequest.objects.all()
    a.delete()
    # b=Login.objects.filter(usertype="worker")
    # b.delete()
    
def deletecontractor(request):
    id = request.GET.get("id")
    contractor= Contractor.objects.filter(id=id).delete()
    login_delete = Login.objects.filter(id=id).delete()
    messages.info(request, 'contractor application deleted')
    return redirect('/adminviewcontractor')


def adminviewworker(request):
    work=Worker.objects.all()
    return render(request, 'admin/viewworker.html',{'work':work})


def actionworker(request):
    status=request.GET['status']
    id=request.GET['id']
    work=Login.objects.get(id=id)
    work.is_active=int(status)
    work.save()
    if status == "1":
        messages.info(request,"approved successfully")
    else:
        messages.info(request,"rejected your request")
    return redirect('/adminviewworker')



def deleteworker(request):
    id = request.GET.get("id")
    work = Contractor.objects.filter(id=id).delete()
    login = Login.objects.filter(id=id).delete()
    messages.info(request, 'worker application deleted')
    return redirect('/adminviewworker')

def adminviewuser(request):
    user=User1.objects.all()
    return render(request, 'admin/viewuser.html',{'user':user})


def userrequestwork(request):
    uid=request.session['uid']
    cid=request.GET.get("cid")
    user=User1.objects.get(user=uid)
    contractor=Contractor.objects.get(id=cid)
    

    if request.POST:
        work=request.POST.get("worker") 
        days=request.POST.get("days")
        date=request.POST.get("date")
        location=request.POST.get("location")
        req=request.POST.get("req")
        phone=request.POST.get("phone")

        insert=Userworkrequest.objects.create(user=user,cid=contractor,worktype=work,days=days,location=location,request=req,date=date,phone=phone)
        insert.save()


    return render(request,"user/requestwork.html")


def contractorviewuserrequest(request):
    cid=request.session['uid']
    print(cid,"dfasdfsdgsfdfdf")
    id=Contractor.objects.get(constructor=cid)
    print(id.id)
    view=Userworkrequest.objects.filter(cid=id.id,status="pending")
    return render(request,"contractor/viewuserrequest.html",{'view':view})

def userrequestaction(request):
    status=request.GET['status']
    id=request.GET['id']
    work=Userworkrequest.objects.get(id=id)
    work.status=status
    work.save()
    if status == "accepted":
        messages.info(request,"approved successfully")
    else:
        messages.info(request,"rejected your request")
    return redirect('/contractorviewuserrequest')

    
def userviewstatus(request):
    uid=request.session['uid']
    print(uid,"sdsdasd")
    id=User1.objects.get(user=uid)
    print(id.id,"aaaaabbbbbbbbbbbbbb")
    data=Userworkrequest.objects.filter(user=id)
    data1=AllotedWorks.objects.filter(uid=id.id,status="work done")
    
    return render(request,'user/viewworkstatus.html',{'data':data,'data1':data1})


def contractorviewworker(request):
    work=Worker.objects.all()
    Cid=request.session['uid']
    
    cid=Contractor.objects.get(constructor=Cid)
    rid=request.GET.get('rid')
    uid=request.GET.get('uid')
    Rid=Userworkrequest.objects.get(id=rid)
    Uid=User1.objects.get(id=uid)
        
    
        # data=Worker.objects.get(worker=id)
        # data=Worker.objects.get(worker=wid)
    if request.POST:
        wid=request.POST.get('wid')
        work=Worker.objects.get(id=wid)
       

        insert=AllotedWorks.objects.create(uid=Uid,wid=work,cid=cid,rid=Rid)
        insert.save()
        msg="Work Alloted to Worker"
        return redirect('/contractorviewworker')
    return render(request,'contractor/viewworkers.html',{'work':work})

# def allotwork(request):
#     Cid=request.session['uid']
   
#     cid=Contractor.objects.get(constructor=Cid)
#     rid=request.GET.get('rid')
#     uid=request.GET.get('uid')
    
#     Rid=Userworkrequest.objects.get(id=rid)
#     Uid=Userworkrequest.objects.get(user=id)
#         id=request.GET.get('id')
#         wid=Worker.objects.get(worker=id)
    
    
#     if request.POST:

#         insert=AllotedWorks.objects.create(uid=Uid,wid=wid,cid=cid,rid=Rid)
#         insert.save()
#         msg="Work Alloted to Worker"
#         return redirect('/contractorviewworker')

        
    

    
def workerviewassignedwork(request):
    wid=request.session['uid']
    work=Worker.objects.get(worker=wid)
    print(work.id,"sfdddddda")
    worker=AllotedWorks.objects.filter(wid=work.id)
    return render(request,'worker/allotedwork.html',{'worker':worker})

def assignedaction(request):
    status=request.GET['status']
    id=request.GET['id']
    work=AllotedWorks.objects.get(id=id)
    work.status=status
    work.save()
    if status == "accepted":
        messages.info(request,"accepted successfully")
    elif status == "work done":
        data=Userworkrequest.objects.filter(user=id).update(status="work done")
        messages.info(request,"work completed successfully")
    else:
        messages.info(request,"work rejected")
    return redirect('/workerviewassignedwork')


def contractorviewwork(request):
    cid=request.session['uid']
    print(cid,"aaaaaaaaaaaaaaaaaaa")
    id=Contractor.objects.get(constructor=cid)
    print(id.id,"aaaaaaaaaaaaaaaaa")
    work=AllotedWorks.objects.filter(cid=id.id,status="process")
    work1=AllotedWorks.objects.filter(cid=id.id,status="accepted")
    work2=AllotedWorks.objects.filter(cid=id.id,status="work done")
    return render(request, 'contractor/viewallotedwork.html',{'work':work,'work1':work1,'work2':work2})



def userfeedback(request):
    uid=request.session['uid']
    wid=request.GET.get('wid')
    cid=request.GET.get('cid')
    Uid=User1.objects.get(user=uid)
    Wid=Worker.objects.get(id=wid)
    Cid=Contractor.objects.get(id=cid)
    # Cid=Contractor.objects.get(constructor=cid)
    # print(cid.id,"qqqqqqqqq")
    
    if request.POST:
        msg=request.POST.get('msg')
        
        feedback=Customerfeedback.objects.create(uid=Uid,wid=Wid,cid=Cid,msg=msg)
        feedback.save()
    return render(request,'user/feedback.html')


def workerfeedback(request):
    wid=request.session['uid']
    uid=request.GET.get('wid')
    cid=request.GET.get('cid')
    Wid=Worker.objects.get(worker=wid)
    Uid=User1.objects.get(id=uid)
    Cid=Contractor.objects.get(id=cid)
    # Cid=Contractor.objects.get(constructor=cid)
    # print(cid.id,"qqqqqqqqq")
    
    if request.POST:
        msg=request.POST.get('msg')
        
        feedback=Workerfeedback.objects.create(uid=Uid,wid=Wid,cid=Cid,msg=msg)
        feedback.save()
    return render(request,'worker/feedback.html')
                            
def workerviewfeedback(request):
    wid=request.session['uid']
    Wid=Worker.objects.get(worker=wid)
    feedback=Customerfeedback.objects.filter(wid=Wid)
    return render(request,'worker/viewfeedback.html',{'feedback':feedback})
    
def contractorviewfeedback(request):
    cid=request.session['uid']
    Cid=Contractor.objects.get(constructor=cid)
    feedback=Customerfeedback.objects.filter(cid=Cid)
    feedback1=Workerfeedback.objects.filter(cid=Cid)
    return render(request,'contractor/viewfeedback.html',{'feedback':feedback,'feedback1':feedback1})


def userpayment(request):
    uid=request.session['uid']
    wid=request.GET.get('wid')
    cid=request.GET.get('cid')
    userid=request.GET.get('uid')
    Uid=User1.objects.get(user=uid)
    Wid=Worker.objects.get(id=wid)
    Cid=Contractor.objects.get(id=cid)
    print(uid)
    id=AllotedWorks.objects.get(uid__id=userid)
    payment1=AllotedWorks.objects.filter(uid__id=userid,status="work done")
    
    if request.POST:
        
        
        day=request.POST.get('day')
        amount=request.POST.get('amount')
        
        payment=Customerpayment.objects.create(amount=amount,date=day,uid=Uid,wid=Wid,cid=Cid)
        payment.save()
        data1=Userworkrequest.objects.get(user=Uid)
        data=Userworkrequest.objects.filter(user=Uid).update(payment="paid")
    return render(request,'user/payment.html',{'payment1':payment1})
    
    
    
def userviewpayment(request):
    uid=request.session['uid']
    Uid=User1.objects.get(user=uid)
    payment=Customerpayment.objects.filter(uid=Uid)
    return render(request,'user/viewpayment.html',{'payment':payment})
        
def contractorpayment(request):
    cid=request.session['uid']
    wid=request.GET.get('wid')
    Uid=request.GET.get('Uid')
    id=request.GET.get('cid')
    print(Uid,"ADDDDDDDDDDDD")
    print(wid,'aDSFASFADF')
    Cid=Contractor.objects.get(constructor=cid)
    Userid=User1.objects.get(id=Uid)
    Wid=Worker.objects.get(id=wid)
   
   
    # id=AllotedWorks.objects.get(cid__id=id)
    payment1=AllotedWorks.objects.filter(cid__id=id,status="work done")
    
    if request.POST:
        
        
        day=request.POST.get('day')
        amount=request.POST.get('amount')
        
        payment=Contractorpayment.objects.create(amount=amount,date=day,uid=Userid,wid=Wid,cid=Cid)
        payment.save()
        data1=Userworkrequest.objects.get(user=Uid)
        data=Userworkrequest.objects.filter(user=Uid).update(payment="paid")
        pay=AllotedWorks.objects.filter(cid__id=id,status="work done").update(payments="paid")
        
    return render(request,'user/payment.html',{'payment1':payment1})


def contractorviewpayment(request):
    cid=request.session['uid']
    Cid=Contractor.objects.get(constructor=cid)
    payment=Contractorpayment.objects.filter(cid=Cid)
    return render(request,'contractor/viewpayment.html',{'payment':payment})

def adminviewfeedback(request):
    user=Customerfeedback.objects.all()
    worker=Workerfeedback.objects.all()
    return render(request,'admin/viewfeedback.html',{'worker':worker,'user':user})

def delete1(request):
        a=Login.objects.filter(is_active="0").update(is_active="1")
        
def viewworker(request):
    worker=Worker.objects.all()
    return render(request,'contractor/viewworker1.html',{'worker':worker})


def workerviewcontractor(request):
    contract=Contractor.objects.all()
    return render(request,'worker/viewcontractor.html',{'contract':contract})

def logout(request):
    auth.logout(request)
    return redirect('/')

def contractordeleteworkrequest(request):
    rid=request.GET.get('rid')
    work=Userworkrequest.objects.filter(id=rid)
    work.delete()
    messages.info(request,"userworkrequest deleted successfully")
    return redirect('/contractorviewuserrequest')
    
def workerdeleterequest(request):
    rid=request.GET.get('rid')
    work=AllotedWorks.objects.filter(id=rid)
    work.delete()
    user=Userworkrequest.objects.filter(id=rid).update(status="accepted")
    messages.info(request,"work request deleted successfully")
    return redirect('/workerviewassignedwork')