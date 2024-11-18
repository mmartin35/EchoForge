from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from home.games.combine_box import *
from .forms import DirectionForm, ResetForm

def logout(request):
    logout(request)
    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid login', status=401)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

def combine_box(request):
    board = request.session.get('board', [[1] * 4 for _ in range(4)])
    if request.method == 'POST':
        resetForm = ResetForm(request.POST)
        directionForm = DirectionForm(request.POST)
        if resetForm.is_valid():
            print('reseted')
            board = cb_reset()
        if directionForm.is_valid():
            direction = directionForm.cleaned_data['direction']
            board = game_combine_box(board, direction)
    request.session['board'] = board
    context = {
        'board': board,
    }
    return render(request, 'games/combine_box.html', context)

def sokoban(request):
    context = {
        'board': 'NA',
    }
    return render(request, 'games/sokoban.html', context)
