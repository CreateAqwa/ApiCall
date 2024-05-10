from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

def Home(request):

    a={
        
        'bb':"11",
        'aa':"13",
        "bb":'321',
    }
    
    print(a.__len__())
    return JsonResponse(a)

def home2(request):
    return render(request,'home2.html')



