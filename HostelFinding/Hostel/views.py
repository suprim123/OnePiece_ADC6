from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Hostel
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse, Http404
# from django.contrib.auth.models import User


def hostel_form(request):
    return render(request,'Hostelform.html')



def hostel_save(request):
    if request.method== 'POST': 
        get_Name =request.POST['Name']
        get_Location= request.POST['Location']
        get_Price =request.POST['Price']
        get_Description= request.POST['Description']
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
    return render(request, 'upload.html')
    


# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404


# def view_signup_user(request):
#     if request.method=="GET":
#      return render(request,'templates/registation/signup.html')
#     else
#     print(request.POST)
#     userobj=User.objects.create_user[username=request.POST['input_username'],password=request.POST['input_password']
#     userobj.save()
#     return HttpResponse("Signup Successful")