from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})

def first_loan(request):
    return render(request, 'loans/first_loan_page.html', {})

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    print(message)
    return HttpResponse(message)
