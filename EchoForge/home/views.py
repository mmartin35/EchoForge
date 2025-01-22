from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from home.games.combine_box import *
from home.games.sokoban import *
from .forms import DirectionForm, ResetForm

def logout(request):
    auth_logout(request)  # Utilise le module de logout
    return redirect('login')

def login_view(request):  # Renommé pour éviter le conflit
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Utilise le module login correctement
            return redirect('home')  # Redirection vers 'home' après connexion réussie
        else:
            return HttpResponse('Invalid login', status=401)
    return render(request, 'login.html')  # Retourne la page de login si ce n'est pas une requête POST

@login_required
def home(request):
    return render(request, 'home.html')

def combine_box(request):
    cb_board = request.session.get('cb_board', [[1] * 4 for _ in range(4)])
    cb_score = request.session.get('cb_score', 0)
    if request.method == 'POST':
        resetForm = ResetForm(request.POST)
        directionForm = DirectionForm(request.POST)
        if resetForm.is_valid():
            print('reseted')
            cb_board = int_board_init(4, 1)
        if directionForm.is_valid():
            direction = directionForm.cleaned_data['direction']
            cb_board = game_combine_box(cb_board, direction, cb_score)
    request.session['cb_board'] = cb_board
    context = {
        'board': cb_board,
    }
    return render(request, 'games/combine_box.html', context)

def sokoban(request):
    sokoban_board = request.session.get('sokoban_board', [['#'] * 10 for _ in range(10)])
    if request.method == 'POST':
        resetForm = ResetForm(request.POST)
        directionForm = DirectionForm(request.POST)
        if resetForm.is_valid():
            print('reseted')
            sokoban_board = str_board_init(10, '#')
        if directionForm.is_valid():
            direction = directionForm.cleaned_data['direction']
            sokoban_board = game_sokoban(sokoban_board, direction)
    request.session['sokoban_board'] = sokoban_board
    context = {
        'board': sokoban_board,
    }
    return render(request, 'games/sokoban.html', context)
