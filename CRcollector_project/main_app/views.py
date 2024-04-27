from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'cr/home.html')

def about(request):
    return render(request, 'cr/about.html')

def cards(request):
    return render(request, 'cr/index.html', {
        'cards': cards
    }) 


