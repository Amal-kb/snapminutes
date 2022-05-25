from ast import And
from logging import exception
import py_compile
from django.contrib import messages
from multiprocessing import context
from sqlite3 import Cursor
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.db import connection
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,Http404,JsonResponse
from.models import(User,user1,admin1,org,usereg,meeting)
from user_interface import summary,summary2
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template.loader import render_to_string





# Create your views here.



def index(request):
    return render(request, template_name="index.html")
     # return HttpResponse("Hello, world. You're at the polls index.")


#Create, Retrieve, Update, Delete ----> CRUD

def form_createView(request, *args, **kwargs):
    template_name = 'user_interface/create.html'
    context = {}
    user = request.user
    if not user.is_authenticated:
        #DO something
        user = "admin"

    

    edu_form = EducationForm(request.POST or None)
    if edu_form.is_valid():
        edu_form.save(commit=False)
        edu_form.user = user
        edu_form.save(request = request)
    else:
        edu_form = EducationForm()

    exp_form = ExperienceForm(request.POST or None)
    if exp_form.is_valid():
        exp_form.save(commit=False)
        exp_form.user = user
        exp_form.save(request = request)
    else:
        exp_form = ExperienceForm()

    project_form = ProjectForm(request.POST or None)
    if project_form.is_valid():
        project_form.save(commit=False)
        project_form.user = user
        project_form.save(request = request)
    else:
        project_form = ProjectForm()
    
    skill_form = SkillsetForm(request.POST or None)
    if skill_form.is_valid():
        skill_form.save(commit=False)
        skill_form.user = user
        skill_form.save(request = request)
    else:
        skill_form = SkillsetForm()

    context = {
        'user': user,
        'eduFORM': EducationForm(),
        'expFORM': ExperienceForm(),
        'projectFORM': ProjectForm(),
        'skillFORM': SkillsetForm(), # skill_form,
    }

    return render(request, template_name, context)










def login_view(request,*args,**kwargs):
    if request.method=="POST":
        #attempt the user to sign in
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)

        #check if authentication is successfull
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"user_interface/loginRegister.html",{"message":"password must match."})
    else:
        return render(request,"user_interface/loginRegister.html",{"message":""})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        emp_org=request.POST['emp_org']
        password=request.POST['password']
        

        ins=RegistModel(username=username,email=email,phone=phone,emp_org=emp_org,password=password)
        ins.save()
        print("the data has been written to the db")
    #form=RegisterModelForm(request.POST or None)
    #if(form.is_valid()):
        #form.save()
    return render(request,'loginRegister.html')

def createmeeting(request):
    #if request.method=='POST':
    #username=request.POST['username']
    #email=request.POST['email']
    #phone=request.POST['phone']
    #emp_org=request.POST['emp_org']
    #password=request.POST['password']

    #ins=RegistModel(username=username,email=email,phone=phone,emp_org=emp_org,password=password)
    #ins.save()
    #print("the data has been written to the db")
    #form=RegisterModelForm(request.POST or None)
    #if(form.is_valid()):
        #form.save()"""
    return render(request,'user_interface/createmeeting.html')

def sample(request):
    if request.method=='POST':
        sql="INSERT INTO Persons VALUES (42,'jjkh','ggkkj','hjhll','jhjkk')"
        cursor=connection.cursor()
        cursor.execute(sql)
    return render(request,'user_interface/sample.html')


#-----------------------------------------

def adminLogin(request):
    return render(request,'adminLogin.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def adminSignup(request):
    return render(request,'adminSignup.html')

def adminSignupFun(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        orgname=request.POST['orgname']
        password=request.POST['pass']
        cpassword=request.POST['cpass']

        admin = admin1.objects.all()

        for a in admin:
            if(a.adminname==name):
                messages.info(request, 'admin name already exist!')
                return render(request,'adminSignup.html')
            if(a.email==email):
                messages.info(request, 'This email already registered!')
                return render(request,'adminSignup.html')
            if(a.orgname==orgname):
                messages.info(request, 'Organization Name already registered!')
                return render(request,'adminSignup.html')
        
        if(password == cpassword):
            ins=org(orgname=orgname)
            ins.save()
            orgid = org.objects.latest('orgid')

            user = admin1(adminname=name,email=email,phone=phone,password=password,orgname=orgname,orgid=orgid)
            user.save()
            messages.success(request, 'Successfully registered, You can Login Now..')
            return adminLogin(request)
        else:
            messages.info(request, 'Password and Re-entered password must be same.')
            return render(request,'adminSignup.html')
    else:
        return render(request,'adminSignup.html')



    

def userLogin(request):
    return render(request,'userLogin.html')

def minutes(request):
    return render(request,'minutes.html')

def userSignupFun(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user = user1.objects.all()

        for a in user:
            if(a.username==name):
                messages.info(request, 'User name already exist!')
                return render(request,'userLogin.html')
            if(a.email==email):
                messages.info(request, 'This email already registered!')
                return render(request,'userLogin.html')
 
        
        if(password == cpassword):

            user = user1(username=name,email=email,phone=phone,password=password)
            user.save()
            messages.success(request, 'Successfully registered, You can Login Now..')
            return userLogin(request)
        else:
            messages.info(request, 'Password and Re-entered password must be same.')
            return render(request,'userLogin.html')
    else:
        return render(request,'userLogin.html')



def adminDashboard(request):
    if 'aemail' in request.session:
        email=request.session['aemail']
        admin=admin1.objects.get(email=email)
        orgid=admin.orgid_id
        orgname=admin.orgname
        c=0
        meet=meeting.objects.all()

        for m in meet:
            if(m.orgid_id==orgid):
                c=c+1
            

        user = user1.objects.all()
        userreg = usereg.objects.all()
        m=0
        userlist=[]
        for u in userreg:
            if(u.orgid_id==orgid):
                userlist.append(u.email)
                m=m+1

        data = {'meet':meet}
        data['orgid']=orgid
        data['user']=user
        data['userreg']=userreg
        data['orgname']=orgname
        data['total']=c
        data['total2']=m
        request.session['userlist']=userlist
        return render(request,'adminDashboard.html',context=data)
    else:
        messages.info(request, 'You need to login first')
        return render(request,'adminLogin.html')

def userdashboard(request):
    if 'uemail' in request.session:
        email=request.session['uemail']
        user=user1.objects.get(email=email)
        userid=user.userid

        userreg = usereg.objects.all()
        meet = meeting.objects.all()
        org1 = org.objects.all()

        c=0
        list=[]
        for u in userreg:
            if u.userid_id==userid:
                list.append(u.orgid_id)
        
        for i in list:
            for m in meet:
                if m.orgid_id==i:
                    c=c+1
                
        
       
        data = {'meet':meet}
        data['orglist']=list
        data['total']=c
        data['org']=org1
      
        return render(request,'userdashboard.html',context=data)
    else:
        messages.info(request, 'You need to login first')
        return render(request,'userLogin.html')


def adminedit(request):
    return render(request,'adminedit.html')

def attend(request):
    if 'aemail' in request.session:
        email=request.session['aemail']
        admin=admin1.objects.get(email=email)
        orgid=admin.orgid_id
        userreg = usereg.objects.all()
        meet = meeting.objects.all()

        data = {'orgid':orgid}
        data['userreg']=userreg
        data['meet']=meet

        return render(request,'attendance.html',context=data)
    else:
        messages.info(request, 'You need to login first')
        return render(request,'adminLogin.html')

def attendfunc(request):
    if 'aemail' in request.session:
        mid = request.POST.get('mid')
        print(mid)
        meeting_id=meeting.objects.get(meetingid=mid)
        absent = request.POST.getlist('checks[]')
        mystring=','.join(str(e) for e in absent)
        meeting_id.absentees=mystring
        meeting_id.save()
       
        messages.info(request, 'Attendance marked Successfully...')
        return attend(request)
    else:
        messages.info(request, 'You need to login first')
        return render(request,'adminLogin.html')

def useredit(request):
    return render(request,'useredit.html')

def speechgen(request):
    email=request.session['aemail']
    admin=admin1.objects.get(email=email)
    orgid=admin.orgid_id
    meet = meeting.objects.all()

    data = {'orgid':orgid}
    data['meet']=meet

    return render(request,'speech.html',context=data)

def speechgenFun(request):
    if request.method=='POST':
        text=request.POST['speech']
        agenda=request.POST['agenda']
        number=request.POST['number']
        
        print(number)

        request.session['text'] = text
        request.session['agenda'] = agenda
        request.session['number'] = number
        return summary2.summarygenFun(request)

    return render(request,'speech.html')

def summeryadd(request):
    if request.method=='POST':
        speech=request.POST['speech']
        meetingid2=request.POST['meetingid']
        meetingid=int(meetingid2)
        meet = meeting.objects.get(meetingid=meetingid)
        meet.speech=speech
        meet.save()

        email=request.session['aemail']
        admin=admin1.objects.get(email=email)
        orgid=admin.orgid_id
        meet = meeting.objects.all()

        data = {'orgid':orgid}
        data['meet']=meet
        messages.info(request, 'Meeting summery Added to Meeting Id:'+meetingid2+'')
        return render(request,'speech.html',context=data)
  
    return render(request,'speech.html')

def users(request):
    if 'aemail' in request.session:
        email=request.session['aemail']

        admin = admin1.objects.get(email=email)
        orgid=admin.orgid_id

        user = user1.objects.all()
        userreg = usereg.objects.all()
        
        data = {'orgid':orgid}
        data['user']=user
        data['userreg']=userreg
        return render(request,'users.html',context=data)
    else:
        messages.info(request, 'You need to login first')
        return render(request,'adminLogin.html')

def user_add(request):
    if request.method=='POST':
        email=request.POST['email']

        try:
            user = user1.objects.get(email=email)
            userid2=user.userid
            username1=user.username
            aemail=request.session['aemail']
            admin = admin1.objects.get(email=aemail)
            orgid=admin.orgid_id
            try:
                userreg = usereg.objects.get(email=email,orgid=orgid)
                messages.info(request, 'User Already Exist..')
                return users(request)
            except Exception as e:
                userreg = usereg(orgid_id=orgid,username=username1,email=email,userid_id=userid2)
                userreg.save()

                messages.info(request, 'Added Successfully..')
                return users(request)         
                       

        except Exception as e:
            aemail=request.session['aemail']
            admin = admin1.objects.get(email=aemail)
            orgid=admin.orgid_id
            user = user1(username="guest",email=email,password="abc")
            user.save()
            userreg = usereg(orgid_id=orgid,email=email,userid_id=user.userid)
            userreg.save()
            messages.info(request, 'Guest user added')
            return users(request)
    else:
        return users(request)

def db_delete_user(request,id):
    aemail=request.session['aemail']
    admin = admin1.objects.get(email=aemail)
    orgid = admin.orgid_id
    userreg = usereg.objects.all()
    for u in userreg:
        x=int(u.userid_id)
        y=int(id)

        if(x==y):
            if(u.orgid_id==orgid):
                u.delete()
                messages.info(request, 'user deleted successfuly..')
                return users(request)
    return HttpResponse("Something went wrong!!!!!")

def meeting_edit_admin(request,id):
    meet = meeting.objects.get(meetingid=id)
    data = {'meet':meet}

    return render(request,'adminedit.html',context=data)

def meeting_delete(request,id):
    aemail=request.session['aemail']
    admin = admin1.objects.get(email=aemail)
    orgid = admin.orgid_id
    y=int(id)
    print(y)
    meet=meeting.objects.all()
    for m in meet:
        if m.meetingid==y:
            m.delete()
    meet2=meeting.objects.all()
    data = {'meet':meet2}
    data['orgid']=orgid
    return render(request,'meeting.html',context=data)


def meeting_view_admin(request,id):
    meet = meeting.objects.get(meetingid=id)
    user = user1.objects.all()
    absent=meet.absentees
    absentlist = absent.split(",")
    test_list = [int(i) for i in absentlist]
    print(test_list)
    strlist=[]
    c=0
    for u in user:
        if u.userid in test_list:
            if u.username=='guest':
                strlist.append(u.username+'('+ u.email +')')
            else:
                strlist.append(u.username)
    
    print(strlist)
    listToStr = ','.join(map(str,strlist))
    data = {'meet':meet}
    data['listToStr']=listToStr


    

    return render(request,'minutes.html',context=data)

def admin_logout(request):
    if 'aemail' in request.session:
        del request.session['aemail']
        return render(request,'adminLogin.html')
    if 'uemail' in request.session:
        del request.session['uemail']
        return render(request,'userLogin.html')
    
    else:
        return render(request,'adminLogin.html')


    

def update_meeting_admin(request):
    if request.method == 'POST':
        meetingleader = request.POST.get('meetingleader')
        secretary = request.POST.get('secretary')
        date = request.POST.get('date')
        time = request.POST.get('time')
        place = request.POST.get('place')
        agenda = request.POST.get('agenda')
        mid = request.POST.get('meetingid')

        
        meet=meeting.objects.get(meetingid=mid)
        meet.meetingleader=meetingleader
        meet.secretary=secretary
        meet.date=date
        meet.time=time
        meet.place=place
        meet.agenda=agenda
        meet.save()

        messages.info(request, 'Meeting Updated successfuly')
        return meetings(request)
    
    else:
        return HttpResponse("Something went wrong!!!!!")

        
            





def login_admin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        admin = admin1.objects.all()

        for a in admin:
            if(a.email==email):
                if a.password == password:
                    request.session['aemail'] = a.email
                    return adminDashboard(request)
                else:
                    messages.info(request, 'Incorrect Password!!!')
                    return render(request,'adminLogin.html')
        
        messages.info(request, 'Invalid admin name!!!')
        return render(request,'adminLogin.html')
    
    else:
        return HttpResponse("Something went wrong faffsffa!!!!!")


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = user1.objects.all()

        for a in user:
            if(a.email==email):
                
                if a.password == password:
                    print("hellop")
                    request.session['uemail']=a.email
                    print(request.session['uemail'])
                    return userdashboard(request)
                else:
                    messages.info(request, 'Incorrect Password!!!')
                    return render(request,'userLogin.html')
        
        messages.info(request, 'Invalid User name!!!')
        return render(request,'userLogin.html')
    
    else:
        return HttpResponse("Something went wrong faffsffa!!!!!")


def meetings(request):
    if 'aemail' in request.session:
        email=request.session['aemail']
        admin=admin1.objects.get(email=email)
        orgid=admin.orgid_id

        meet=meeting.objects.all()

        data = {'meet':meet}
        data['orgid']=orgid

        return render(request,'meeting.html',context=data)
    else:
        messages.info(request, 'You need to login first')
        return render(request,'adminLogin.html')




def admin_meeting_add(request):
    if request.method == 'POST':
        meetingleader = request.POST.get('meetingleader')
        secretary = request.POST.get('secretary')
        date = request.POST.get('date')
        time = request.POST.get('time')
        place = request.POST.get('place')
        agenda = request.POST.get('agenda')
        print(agenda)

        aemail=request.session['aemail']
        admin=admin1.objects.get(email=aemail)
        orgid=admin.orgid_id
        userreg = usereg.objects.all()
        userlist=[]
        for u in userreg:
            if(u.orgid_id==orgid):
                userlist.append(u.email)

        
        meet=meeting(meetingleader=meetingleader,secretary=secretary,date=date,time=time,place=place,agenda=agenda,orgid_id=orgid)
        meet.save()
        try:
            subject = 'Meeting Scheduled'
            message = "Hi\nNew meeting scheduled for you.\n meetingleader:"+ meetingleader + "\nsecretary:"+secretary+"\n date:"+date+"\n time:"+time+"\n place:"+place+"\n agenda:"+agenda+""
            msg_html = render_to_string('email.html')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = userlist
            send_mail( subject, message, email_from, recipient_list,html_message=msg_html,fail_silently=False)
        except exception as e:
                return HttpResponse("Invalid header found.")


        messages.info(request, 'Meeting created successfuly')
        return meetings(request)
    
    else:
        return HttpResponse("Something went wrong!!!!!")
    

def add_meeting_user(request):
    if request.method == 'POST':
        meetingleader = request.POST.get('meetingleader')
        secretary = request.POST.get('secretary')
        date = request.POST.get('date')
        time = request.POST.get('time')
        place = request.POST.get('place')
        agenda = request.POST.get('agenda')
        orgid = request.POST.get('id')


        
        meet=meeting(meetingleader=meetingleader,secretary=secretary,date=date,time=time,place=place,agenda=agenda,orgid_id=orgid)
        meet.save()

        messages.info(request, 'Meeting created successfuly')
        return useredit(request)
    
    else:
        return HttpResponse("Something went wrong!!!!!")