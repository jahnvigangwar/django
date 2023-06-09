from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable" : "sending variable"
    }
    return render(request, 'index.html', context)
    # return HttpResponse('this is hime page')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('this is ABOUT page')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('this is ABOUT page')


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse('this is CONTACT page')