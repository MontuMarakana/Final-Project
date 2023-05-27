from django.shortcuts import render, HttpResponse,redirect
from .models import *
from .forms import signupForm
from django.contrib.auth import logout



# Create your views here.

"""def index(request):
    if request.method=='POST':
        myfrm=signupForm(request.POST)
        if myfrm.is_valid():
            myfrm.save()
            print("Signup Successfully")
            return redirect('/')
        else:
            print(myfrm.errors)
    else:
        myfrm=signupForm()
    return render(request,'index.html',{'myfrm':myfrm})"""





# Create your views here.
# def index(request):
#     if request.method=='POST':
#         signupfrm=signupForm(request.POST)
#         if signupfrm.is_valid():
#             signupfrm.save()
#             print("Signup Successfully!")
#             return render(request,'index.html')
#         else:
#             print(signupfrm.errors)
    
#     return render(request,'index.html')

# def userlogin(request):
#     if request.method=='POST':
#         unm=request.POST['username']
#         pas=request.POST['password']

#         user=signupForm.objects.filter(username=unm,password=pas)
#         if user: 
#             print("Login Successfull!")
#             request.session['user']=unm 
#             return redirect('home')
#         else:
#             print("Error! Login fail")
#     return render(request,'userlogin.html')

def home(request):
    data=request.session.get('user')
    return render(request,'home.html',{'data':data})

def profile(request):
    data=request.session.get('user')
    return render(request,'profile.html',{'data':data})

def contact(request):
    data=request.session.get('user')
    return render(request,'contact.html',{'data':data})

def userlogout(request):
    logout(request)
    return redirect('index.html')


def index(request):
    if request.method == 'POST':
        signupfrm = signupForm(request.POST)
        if signupfrm.is_valid():
            signupfrm.save()
            print("Signup Successfully!")
            return render(request, 'index.html')
        else:
            print(signupfrm.errors)

    return render(request, 'index.html', {'signupfrm': signupForm()})

def userlogin(request):
    if request.method == 'POST':
        unm = request.POST['username']
        pas = request.POST['password']
      

        user = signupForm.objects.filter(username=unm, password=pas)
        if user:
            print("Login Successful!")
            request.session['user'] = unm
            return redirect('home')
        else:
            print("Error! Login failed")

    return render(request, 'userlogin.html')

