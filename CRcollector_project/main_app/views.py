from django.shortcuts import render, redirect
from .models import Card, Player
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import StatusForm
from django.views.generic import ListView, DetailView


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
    players = Player
    id_list = card.players.all().values_list('id')
    buddies_card_is_not_assoc = Player.objects.exclude(id__in=id_list)
    status_form = StatusForm()
    return render(request, 'cr/detail.html', {'card':card, 'status_form': status_form, 'players': buddies_card_is_not_assoc})

def add_status(request, pk):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.card_id = pk
        new_status.save()
    return redirect('details', card_id=pk)

def assoc_player(request, pk, player_pk):
    Card.objects.get(id=pk).players.add(player_pk)
    return redirect('details', card_id=pk)

def assoc_delete(request, pk, player_pk):
    Card.objects.get(id=pk).players.remove(player_pk)
    return redirect('details', card_id=pk)

class CardCreate(CreateView):
    model = Card
    fields = ['name','rarity','cost']

class CardUpdate(UpdateView):
    model = Card
    fields = ['name','rarity','cost']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'

class PlayerList(ListView):
    model = Player

class PlayerDetail(DetailView):
    model = Player

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = ('player_name', )

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players'