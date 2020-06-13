from django.http import HttpResponse
from django.shortcuts import render , redirect
from ecommerce.forms import UserProfileForm , UserForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ecommerce.models import UserProfile



def homepage(request):
    return render(request,'homepage.html')


def register(request):
    up=UserForm()
    upf=UserProfileForm()
    if request.method == 'POST':
        user=UserForm(request.POST)
        pro=UserProfileForm(request.POST)
        # if pro.is_valid():
        #     return HttpResponse("user is valid")
        # else:
            # return HttpResponse(pro.errors)
        if user.is_valid() and pro.is_valid():
            # return HttpResponse('forms are valid')
            usersaved=user.save()
            usersaved.set_password(usersaved.password)
            usersaved.save()
            prosaved=pro.save(commit=False)
            prosaved.user=usersaved
            prosaved.save()
            new_user = authenticate(username=user.cleaned_data['username'],
                                    password=user.cleaned_data['password'],)
            login(request, new_user)
            return redirect('buyer:buyerapp')
        else:
            print(user)
            return render(request,'register.html',{'form1':up,'form2':upf})
            # return render(request,'register.html')
            # return HttpResponse("Inavalid Sahi karo")
    return render(request,'register.html',{'form1':up,'form2':upf})
    # return render(request,'register.html')

def login_call(request):
    if request.method == 'POST':
        username = request.POST['usernm']
        password = request.POST['passwd']
        selecteduser = authenticate(username = username,password = password)
        if selecteduser:
            if selecteduser.is_active:
                login(request,selecteduser)
                udata = UserProfile.objects.get(user__username=request.user)
                return redirect('buyer:buyerapp')
                # if udata.usertype == 'buyer':
                #     # return redirect('/buyer/buyerapp/')
                #     try:
                #         return redirect(request.GET['next'])
                #     except:
                #         return redirect('buyer:buyerapp')
                    
                # else:
                #     return redirect('/seller/sellerapp/')
            else:
                return HttpResponse("<h1>User deactivated</h1>")
        else:
            return HttpResponse("<h1>Login Failed</h1>")
    else:
        return render(request,'login_call.html')

@login_required
def logout_call(request):
    logout(request)
    return redirect('/')

