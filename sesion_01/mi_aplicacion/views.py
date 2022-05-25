import random

from django.http import JsonResponse
from django.shortcuts import render


def hola_mundo(request):
    context = {"lucky_number": random.randint(1, 10)}
    return render(request, "hola_mundo.html", context)


def suma(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']

    num1 = int(num1)
    num2 = int(num2)

    return JsonResponse({"resultado": num1 + num2})
