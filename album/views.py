from django.shortcuts import render
from django.views.generic import ListView

from album.models import Team, Player

# Create your views here.

class TeamListView(ListView):
    model = Team

class PlayerListView(ListView):
    model = Player