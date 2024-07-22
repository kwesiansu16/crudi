from django.shortcuts import render,HttpResponse

# Create your views here.
def homePageview(request):
    h1 = '<h2>Welcome to the world</h2>'
    return HttpResponse(h1)

def aboutPageView(request):
    return HttpResponse('<h3>Hello how is everything</h3>')