from django.shortcuts import render
from django.views.generic import ListView, DetailView

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