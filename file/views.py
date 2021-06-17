from .forms import FileForm
from django.http.request import HttpRequest
from django.http.response import FileResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import File, Download
from django.contrib import messages
from django.contrib.auth.models import User
import os
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

# Create your views here.


def Home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request,"home/about.html")
def plans(request):
    return render(request,"home/plans.html")

@login_required(login_url='login')
def file(request):
    return render(request, "file.html")


def upload_file(request):
    form = FileForm()
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        
        if form.is_valid():
            fileobj = request.FILES.get('path')
            size = fileobj.size
            ctype = fileobj.content_type
            fd = form.save(commit=False)
            fd.extension = ctype
            fd.size = size
            fd.save()
            messages.success(request,'file uploaded')
            return redirect("views")
    ctx = {'form':form}
    return render(request, "file/upload.html",ctx)


def profile(request):

    return render(request, "file/profile.html")

@login_required
def views(request):
    file = File.objects.all()
    return render(request, "file/views.html", {"file": file})


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            pass
        pass
    else:
        return HttpResponseRedirect('/login/')


def download(request,pk):
    # try
    file = File.objects.get(pk=pk)
    context = {
        'file':file,
    }
    return render(request,'file/download.html',context)
    # except Exception as e:
    #     print(e)
    #     return redirect('views')

def download_item(request, id): 
    item = get_object_or_404(File, pk=id) 
    file_name, file_extension =os.path.splitext(item.path.file.name) 
    file_extension = file_extension[1:] # removes dot 
    response = FileResponse(item.path.file, content_type = "file/%s" % file_extension) 
    response["Content-Disposition"] = "attachment;filename=%s.%s" %(slugify(item.path.name)[:100], file_extension) 
    return response