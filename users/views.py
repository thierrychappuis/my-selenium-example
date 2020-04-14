from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return render(request, 'users/profile.html')

def create_account(request):
    return render(request, 'users/create_account.html')

