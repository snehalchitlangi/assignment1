from django.shortcuts import render



from django.http import HttpResponse



# Create your views here.



def  cse(request):

    return HttpResponse("Welcome on CSE page")



def  etc(request):

    return HttpResponse("Welcome on ETC page")



def  mech(request):

    return HttpResponse("Welcome on MECH page")



def  civil(request):

    return HttpResponse("Welcome on CIVIL page")
