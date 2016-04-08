from home.forms import  UserProfileForm
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import Template, Context
from home.models import Question_ans_key,UserProfile,Submission
import os
import datetime,time
def home_page(request,offset):
       hk="offline"
       if "username" in request.session:
            hk="online"
            username=request.session["username"]
            user=UserProfile.objects.get(username=username)

            offset=int(offset)
            fques=open("/home/siddharth/Desktop/ques","r")
            ques1=fques.readlines()[offset-1]
            fques.close()
            ques1="Q"+str(offset)+": "+ques1

            flag=0
            file_name="/home/siddharth/Desktop/submit/"+username
            file_name="_".join(file_name.split(" "))
            fans=open(file_name,"r")
            prevans=fans.readlines()[offset-1]
            prevans='\r\n'.join(prevans.split('\x0c'))
            prevans='\''.join(prevans.split('\x0b'))
            prevans='\\'.join(prevans.split('NNNNNN'))
            if prevans!='Copy-paste your command here\n':
                if offset>9:
                    prevans=prevans[12:]
                else:
                    prevans=prevans[11:]    
            if 'submit' in request.POST:
                ans=request.POST.get('answ')
                if ans =="":
                    ans=prevans
                prevans=ans
                if prevans!='Copy-paste your command here\n':
                    flag=1
                ans='\x0c'.join(ans.split('\r\n'))
                ans='\x0b'.join(ans.split('\''))
                ans='NNNNNN'.join(ans.split('\\'))
                ans="Answer no"+str(offset)+" "+ans
                x="Answer Saved"
                
                
            elif 'back' or 'next' in request.POST:  
                ans=prevans
                if prevans!='Copy-paste your command here\n':
                    flag=1
                x=""   
            elif 'back' or 'next' in request.GET:  
                ans=prevans
                if prevans!='Copy-paste your command here\n':
                    flag=1
                x=""    
            else:
                ans=prevans
                x=""
            
            string="sed -i \'"+str(offset)+"s\a.*\a"+ans+"\a\' "+file_name
            os.system(string)   
            if offset==1:
                back_value,next_value=0,1
            elif offset==20:
                back_value,next_value=1,0
            else:
                back_value,next_value=1,1 

            back="/home/"+(str(offset-1))+("/")
            nex="/home/"+(str(offset+1))+("/")
            submit="/home/"+(str(offset))+("/")

            maindata={'username':username,'hk':hk,'ques1':ques1,'flag':flag,'x':x,'offset':offset,'prevans':prevans,'next':nex,'submit':submit,'back':back,'next_value':next_value,'back_value':back_value,'string':string}
            context=RequestContext(request,maindata)
            return render_to_response('home/home_page.html',context)

       else:
	  	context=RequestContext(request)
      		return render_to_response('home/home_page.html',context)

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    registered = False
    profile_form = UserProfileForm()
    if request.method == 'POST':
        #user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if  profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.save()
            registered = True
            username=request.POST["username"]
            request.session["username"]=username
            file_name="/home/siddharth/Desktop/submit/"+username
            file_name="_".join(file_name.split(" "))
            f=open("/home/siddharth/Desktop/ques","r")
            fans=open(file_name,"w")
            for i in range(f.readline().len):
                fans.write("Copy-paste your command here")
                fans.write("\n")
            return HttpResponseRedirect('/home/1/')

        else:
            print  profile_form.errors
            return render_to_response(
                'home/register.html',
                { 'profile_form': profile_form, 'registered': registered},
                context)

    else:
        return render_to_response(
                'home/register.html',
                { 'profile_form': profile_form, 'registered': registered},
                context)

def user_login(request):
    context = RequestContext(request)
    exception=""
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            if UserProfile.objects.get(username=username,password=password):
                user=UserProfile.objects.get(username=username,password=password)
                request.session["username"]=user.username
                return HttpResponseRedirect('/home/1/')
            else:        
                print "Invalid login details: {0}, {1}".format(username, password)
                return HttpResponse("Invalid login details supplied.")
        except UserProfile.DoesNotExist:
            exception="Incorrect Username/Password"
            return render_to_response('home/login.html', {'exception':exception}, context)
    else:
        return render_to_response('home/login.html', {'exception':exception}, context)

def submit_ans(request):
    if request.method=='POST':
        #ans=request.POST['ans']
        username=request.session["username"]
        user=UserProfile.objects.get(username=username)
        

    return HttpResponseRedirect("/home/1/")   


def logout(request):
    del request.session["username"]
    return HttpResponseRedirect('/home/1/')

def user_profile(request):
    context=RequestContext(request)
    return render_to_response('home/1.html',{},context)

