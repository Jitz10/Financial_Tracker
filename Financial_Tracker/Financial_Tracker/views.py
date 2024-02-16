from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.core.exceptions import ValidationError
import random

# Use Django Rest Framework for serialization
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_data(request):
    income = random.randint(500, 1500)
    expense = random.randint(300, 700)
    balance = income - expense

    data = {
        'income': income,
        'expense': expense,
        'balance': balance,
        'graphImageUrl': 'https://picsum.photos/200',
    }

    return JsonResponse(data)

def add(request):
    n1 = int(request.GET['num1'])
    n2 = int(request.GET['num2'])
    ans = n1+n2
    data = {
        'ans' : ans,
    }
    return render(request,"add.html",data)