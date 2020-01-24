from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Hostel
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required




def Hostel_form(request):
    return render(request, 'form.html')

def homepage(request):
    return render(request,'')




def hostel_save(request):
    print(request.POST)
    if request.method == 'POST': 
        get_Name =request.POST['Name']
        get_Location= request.POST['Location']
        get_Price =request.POST['Price']
        get_Description= request.POST['Description']
        # get_Picture = request.POST['Picture']
        Hostel_obj = Hostel(Name=get_Name,Location=get_Location,Price=get_Price,Description=get_Description)
        Hostel_obj.save()
        return HttpResponse("Record saved")
    else:
        return HttpResponse("Error record saving")


def hostel_list(request):
    list_of_Hostels= Hostel.objects.all()
    context_variable = {
        'Hostel':list_of_Hostels
    }
    return render(request,'Hostel.html',context_variable)

def hostel_edit(request, ID):
    hostel_obj = Hostel.objects.get(id=ID)
    context_varible = {
        'Hostel':hostel_obj
    }
    return render(request,'Hostelupdateform.html',context_varible)

def hostel_update_save(request,ID):
    hostel_obj = Hostel.objects.get(id=ID)
    hostel_form_data = request.POST
    print(hostel_form_data) 
    hostel_obj.Name = request.POST['Name']
    hostel_obj.Location =request.POST['Location']
    # hostel_obj. Picture = request.POST['Picture']
    hostel_obj. Price = request.POST['Price']
    hostel_obj. Description = request.POST['Description']
    hostel_obj.save()

    return HttpResponse("Record Updated!!")


def hostel_delete(request,ID):
        hostel_obj= Hostel.objects.get(id=ID)
        hostel_obj.delete()
        return HttpResponse("Record Delete!!")

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
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse("Signup Successful")


def view_authenticate_user(request):
    if request.method =="GET":
        return render (request,'Registration/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user)
            return render(request,"hostel.html")
        else:
            return HttpResponse("Authentication Failed")  


def home(request):
    return render(request,'Registration/home.html ')

def logout(request):
     auth.logout(request)
     return render(request,'Registration/home.html')
 
         
        
    
    

