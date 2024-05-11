from django.shortcuts import render, redirect
from .models import Card
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import StatusForm


# cards = [
#     {'name':'Hog Rider', 'level': '5', 'rarity': 'rare', 'cost': 4}, 
#     {'name':'Witch', 'level': '12', 'rarity': 'epic', 'cost': 5}, 
#     {'name':'Mini P.E.K.K.A', 'level': '14', 'rarity': 'rare', 'cost': 4},
# ]

# Create your views here.
def home(request):
    return render(request, 'cr/home.html')

def about(request):
    return render(request, 'cr/about.html')

def cards_index(request):
    cards = Card.objects.all() # This is our get() method from our database for all cards. 
    return render(request, 'cr/index.html', {
        'cards': cards
    }) 

def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    status_form = StatusForm()
    return render(request, 'cr/detail.html', {'card':card, 'status_form': status_form})

def add_status(request, pk):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.card_id = pk
        new_status.save()
    return redirect('details', card_id=pk)

class CardCreate(CreateView):
    model = Card
    fields = ['name','level','rarity','cost']

class CardUpdate(UpdateView):
    model = Card
    fields = ['name','level','rarity','cost']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'
