from django.shortcuts import render

# Create your views here.

def status(request):
    d = {}
    return render(request, 'status.html', d)