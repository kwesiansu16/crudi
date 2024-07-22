from django.shortcuts import render,HttpResponse

# Create your views here.
def fView(request):
    h3 = '<h3>A new project is here</h3>'
    return HttpResponse(h3)