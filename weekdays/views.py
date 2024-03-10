from django.http import HttpResponse
from django.shortcuts import render


def weekdays(request):
    return render(request, 'weekdays/weekdays.html')

def uz(request):
    return render(request, 'weekdays/uz.html')
def en(request):
    return render(request, 'weekdays/en.html')
def ru(request):
    return render(request, 'weekdays/ru.html')