from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
#def login(request):
 #   return render(request,'login.html')
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                print('user is created')
                return redirect('/')
        else:
            print('password not matching')
            return redirect('signup')
            #return redirect('/')#that bring the default home page
    else:
        return render(request,'signup.html')




def logout(request):
    auth.logout(request)
    return redirect('/')
