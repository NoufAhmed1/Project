from django.shortcuts import render , reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .form import  addItem , UserForm, ProfileForm ,LoginForm
from .models import Item , UserProfil
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout

def loguot(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    







def loginform(request):
    form = LoginForm()

    if request.method=='POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data['username']
            password =form.cleaned_data['password']  

            user =authenticate(username=username , password=password)
            if user:
                if user.is_active:
                    login(request , user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.error(request,'your account is blocked')  
            else:
                messages.error(request,'invalid username or password')          
    data={
        'form': form
    }


    return render(request, 'login.html' , data)


 
def home(request):
    Items= Item.objects.all()
    data ={
        'Items' : Items

    }

    return render(request, 'home.html' ,data)

def add(request):
    form = addItem()

    if request.method=='POST':
        form =addItem(request.POST)
        if form.is_valid():
            Item=form.save(commit=False)
            if 'picture' in request.FILES:
             Item.picture=request.FILES['picture']
             
            Item.save()
        return HttpResponseRedirect(reverse('home'))

    data={
        'form': form
    }


    return render(request, 'add.html' , data)

def detail(request , no):
    try:
        item =Item.objects.get(id=no)
    except:
        return HttpResponseRedirect(reverse('home'))

    data ={
        'i' : item
    }
    return render(request, 'detail.html', data)



def register(request):
    userform = UserForm()
    profilform =ProfileForm()
    
    if request.method=='POST':
        userform =UserForm(request.POST)
        profilform =ProfileForm(request.POST)
       
        if userform.is_valid() and profilform.is_valid() :
            user=userform.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile =profilform.save(commit=False)
            profile.user= user
            profile.save()
            
        return HttpResponseRedirect(reverse('home'))

    data={
        'userform': userform ,
        'profilform' :profilform
       
    }


    return render(request, 'register.html' , data)


  

   




