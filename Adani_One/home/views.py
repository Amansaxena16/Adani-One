from django.shortcuts import render

def index(request):
    context = {'page' : 'Adani One'}
    return render(request, 'index.html',context)
def vip_services(request):
    context = {'page' : 'VIP Services'}
    return render(request, 'vip_services.html',context)