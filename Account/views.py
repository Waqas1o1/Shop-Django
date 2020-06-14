from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def Register(request):
    return render(request,'account/register.html')
def SiginUp_Handle(request):
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conform_pass = request.POST['conformpassword']
        User.objects.create_user(user,email,password)    
    
    return HttpResponse('ok Register')