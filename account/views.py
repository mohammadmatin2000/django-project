from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login , logout
# ======================================================================================================================
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request=request, user=user)
                    return redirect('/')
        form=AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html',context)
    else:
        return redirect('/')
# ======================================================================================================================
def logout_view(request):
    logout(request)
    return redirect('/')
# ======================================================================================================================
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request, 'accounts/signup.html')
    return redirect('/')
# ======================================================================================================================