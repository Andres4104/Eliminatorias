from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from album.models import Team, Player

# Create your views here.

class TeamDetailView(DetailView):
    model = Team

class PlayerDetailView(DetailView):
    model = Player

class TeamListView(ListView):
    model = Team

class PlayerListView(ListView):
    model = Player

class TeamCreate(CreateView):
    model = Team
    fields = '__all__'

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'