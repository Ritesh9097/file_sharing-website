from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm


# Create your views here.
@login_required
def dashboard(request):
    
    try:
        data =Profile.objects.get(pk=request.user.pk)

        context ={'data':data}
        return render(request, 'user/dashboard.html',context)
    except :
        return redirect('edit_profile')

@login_required
def edit_profile(request):
    try:
        data =Profile.objects.get(pk=request.user.pk)
        if len(data)>0:
            form =  ProfileForm(instance=data[0])
                
        else:
            form = ProfileForm()
    except:
        form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            formdata = form.save(commit=False)
            formdata.user = request.user
            formdata.save()

            return redirect('dashboard')
    context ={'form':form}
    return render(request, 'user/edit_profile.html',context)

def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html',{'form':UserCreationForm})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
        else:
            return render(request, 'user/register.html',{'form':form})