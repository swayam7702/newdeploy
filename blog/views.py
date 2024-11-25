from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from .form import UserRegister
# Create your views here.


def home(request):
    
    return render(request,'index.html')


# def signup(request):
#     form = UserRegister()
    
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             form.save()    
#             return redirect('login')
        
#     return render(request,'signup.html',{'form':form})

from django.contrib import messages

# from django.contrib import messages
# from django.shortcuts import render, redirect
# from .forms import UserRegister  # Assuming you have a UserRegister form
def signup(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            # Add a success message
            messages.success(request, 'Your account has been created successfully!')
            # Instead of redirecting immediately, we just return the same page
            return render(request, 'signup.html', {'form':  UserRegister()})
        
        else:
            messages.error(request, 'There were some errors with your submission. Please try again.')
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserRegister()

    return render(request, 'signup.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth import login,logout

def user_logout(request):
    logout(request)
    
    return redirect('login')
    
def user_login(request):
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            
            if user is not None:
                login(request,user)
                return redirect('home')
            
    return render(request,'login.html',{'form':form})