from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    # if request.method == 'POST':
    #     order_amount = 50000
    #     order_currency = 'INR'
    #     client = razorpay.Client(auth('rzp_test_rIS0VT9V2kU0p7','1YCqjGWIzLlzQxx61AQWOxWd'))
    #     payment = client.order.create({
    #         'amount':order_amount,
    #         'currency':order_currency,
    #         'payment_capture':'1'
    #     })
    return render(request, "home.html")

@csrf_exempt
def success(request):
    return render(request, "success.html")

