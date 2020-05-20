from django.shortcuts import render


def home(request):

    return render(request, 'pur_beurre/home.html')


def legal_notice(request):

    return render(request, 'pur_beurre/legal_notice.html')
