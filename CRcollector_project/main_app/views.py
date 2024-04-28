from django.shortcuts import render


cards = [
    {'name':'Hog Rider', 'level': '5', 'rarity': 'rare', 'cost': 4}, 
    {'name':'Witch', 'level': '12', 'rarity': 'epic', 'cost': 5}, 
    {'name':'Mini P.E.K.K.A', 'level': '14', 'rarity': 'rare', 'cost': 4},
]

# Create your views here.
def home(request):
    return render(request, 'cr/home.html')

def about(request):
    return render(request, 'cr/about.html')

def cards_index(request):
    return render(request, 'cr/index.html', {
        'cards': cards
    }) 


