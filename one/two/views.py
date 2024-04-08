from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is the homepage")
def  about(request):
    return render(request, 'about.html')
    #  return HttpResponse("this is the about page")
 
def services(request):
    return render(request, 'services.html')
    #  return HttpResponse("this is the service page")
def contact(request):
    return render(request, 'contact.html')
    #  return HttpResponse("this is the conatct page")
    
def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def faq(request):
    return render(request, 'faq.html')

def feedback(request):
    return render(request, 'feedback.html')


def complaint(request):
    return render(request, 'complaint.html')


def suggestion(request):
    return render(request, 'suggestion.html')

