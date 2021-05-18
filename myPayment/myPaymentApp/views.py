from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    fields=[{'name':'Medicine', 'img':'blood.png', 'money':'Rs.50'},{'name':'Covid Emergency Equipments', 'img':'oxygen.jpeg', 'money':'Rs.300'},{'name':'Old Age Home', 'img':'old.webp', 'money':'Rs.10'},{'name':'For Homeless', 'img':'homeless_1.jpg', 'money':'Rs.10'},{'name':'Education', 'img':'edu.jpg', 'money':'Rs.10'},{'name':'Orphanage', 'img':'orphan.jpg', 'money':'Rs.10'},{'name':'General Purpose', 'img':'gen.jpg', 'money':'Rs.10'},{'name':'For Free Vaccination', 'img':'vaccinr.jpg', 'money':'Rs.450'}]
    return render(request, "home.html", {'fields':fields})

def about(request):
    return render(request, "about.html")

def fieldsDetail(request):
    return render(request, "fieldsDetail.html")

@csrf_exempt
def success(request):
    return render(request, "success.html")

