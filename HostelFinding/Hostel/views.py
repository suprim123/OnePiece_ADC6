from django.shortcuts import render
from django.http import HttpResponse
from .models import Hostel

def hostel_form(request):
    return render(request,'Hostelform.html')



def hostel_save(request):
    if request.method== 'POST': 
        
        get_Name =request.POST['Name']
        get_Location= request.POST['Location']
        get_Price =request.POST['Price']
        get_Description= request.POST['Description']
        # get_Picture = request.POST['Picture']
        Hostel_obj = Hostel(Name=get_Name,Location=get_Location,Description=get_Description)
        Hostel_obj.save()
        return HttpResponse("Record saved")
    else:
        return HttpResponse("Error record saving")

def hostel_list(request):
    list_of_Hostels= Hostel.objects.all()
    print(list_of_Hostels)
    context_variable = {
        'Hostel':list_of_Hostels
    }
    return render(request,'Hostel.html',context_variable)