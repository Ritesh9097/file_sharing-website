from .forms import FileForm
from django.http.request import HttpRequest
from django.http.response import FileResponse, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import File, Download
from django.contrib import messages
from django.contrib.auth.models import User
import os
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt # new
from django.conf import settings # new
import stripe

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


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        price = request.GET.get('price')
        plan = request.GET.get('plan')
        try:
          
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': plan,
                        'quantity': 1,
                        'currency': 'inr',
                        'amount': price,
                    }
                ],
                customer_email=request.user.email,
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


def success_pay(request):
    messages.success(request,"you have purchase the plan successfully")
    return redirect('home')

def cancel_pay(request):
    messages.error(request,"you have cancel the payment")
    return redirect('home')