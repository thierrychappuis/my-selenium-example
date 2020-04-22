from django.shortcuts import render

def home(request):
    return render(request, 'pur_beurre/home.html')
