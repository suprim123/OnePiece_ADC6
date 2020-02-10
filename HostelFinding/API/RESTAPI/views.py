from django.shortcuts import render
from .models import Host
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create or View Host 
@csrf_exempt
def hostDetail(request):
    if request.method == "GET":
        place=Host.objects.all()
        sub=list(place.values("hostelName","email","location"))
        org={"HostelInfo":sub}
        return JsonResponse(org)

    elif request.method == "POST":
        print(request.body)
        gb=json.loads(request.body)
        Host.objects.create(hostelName=gb['name'],
        email=gb['email'],
        location=gb['location'])
        return JsonResponse({ "message":"data inserted successfully"})

# View, Delete, up specific Host by Id
@csrf_exempt
def hostUD(request,Id):
        luffy=Host.objects.get(id=Id)
        if request.method == "GET":
            return JsonResponse({
            "hostelName":luffy.hostelName,
            "email":luffy.email,
            "location":luffy.location})
        

        elif request.method == "DELETE":
      
            luffy.delete()
            return JsonResponse({"message":"Your request is Deleted"})
            
            
                
        
        elif request.method == "PUT":
            up=json.loads(request.body) 
            luffy.hostelName=up['name']
            luffy.email=up['email'] 
            luffy.location=up['location']
            luffy.save()
            return JsonResponse({"message":"As per you request data is updated Successfully"})


def pagination(request, PAGENO, SIZE):
    skip = SIZE * (PAGENO-1)
    hostel = Host.objects.all()[skip:PAGENO*SIZE]
    dict={
        "hostel":list(hostel.values("hostelName", "email", "location"))
    }
    return JsonResponse(dict)





    




