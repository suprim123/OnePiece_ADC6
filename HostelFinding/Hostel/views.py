from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .models import Hostel
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout



def homepage(request):
    return render(request,'')




def Hostel_form(request):
    if request.method == 'POST': 
        get_Name =request.POST['Name']
        get_Location= request.POST['Location']
        get_Price =request.POST['Price']
        get_Description= request.POST['Description']
        Hostel_obj = Hostel(Name=get_Name,Location=get_Location,Price=get_Price,Description=get_Description)
        Hostel_obj.save()
        return redirect('Hostel:list')
       
    else:
       return render(request, 'form.html')


def hostel_list(request):
    list_of_Hostels= Hostel.objects.all()
    
    return render(request,'Hostellist.html',{'hostels':list_of_Hostels})



def hostel_edit(request, ID):
    hostel_obj = Hostel.objects.get(id=ID)
    context_varible = {
        'Hostel':hostel_obj
    }
    return render(request,'Hostelupdateform.html',context_varible)

def hostel_update_save(request,ID):
    list_of_Hostels= Hostel.objects.all()
    hostel_obj = Hostel.objects.get(id=ID)
    hostel_form_data = request.POST
    print(hostel_form_data) 
    hostel_obj.Name = request.POST['Name']
    hostel_obj.Location =request.POST['Location']
    # hostel_obj. Picture = request.POST['Picture']
    hostel_obj. Price = request.POST['Price']
    hostel_obj. Description = request.POST['Description']
    hostel_obj.save()
    return redirect('Hostel:list')
    return HttpResponse("Record Updated!!")


def hostel_delete(request, ID):
    hostel = Hostel.objects.get(id=ID)
    hostel.delete()
    return redirect('Hostel:list')
 


def search(request):
        hostel_id = request.GET['location']
        print(hostel_id)
        hostel = Hostel.objects.filter(Location__contains=hostel_id)
        return HttpResponse("TEst")
        #return render(request, 'hostel.html', {'hostel': hostel, 'Location': hostel_id})

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_object = FileSystemStorage()
        file_object.save(uploaded_file.name, uploaded_file)
    return render(request, 'hostelform.html')


def view_register_user(request):
    if request.method =="GET":
        return render(request,'Registration/signup.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
        user.save()
        return render (request,'Registration/login.html')
        return HttpResponse("Signup Successful")


def view_authenticate_user(request):
    if request.method =="GET":
        return render (request,'Registration/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect("/hostellist/")
        else:
           return render (request,'Registration/login.html') 


def home(request):
    return render(request,'Registration/home.html ')

def logout(request):
     auth.logout(request)
     return render(request,'Registration/home.html')
 
def hostel_login(request):
    return render(request,'Registration/login.html')         
        
    
    

