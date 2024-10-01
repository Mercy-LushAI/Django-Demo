from django.shortcuts import render
from django.http import HttpRequest

rooms = [
    {'id': 1, 'name' : 'Lets learn python'},
    {'id': 2, 'name' : 'Lets learn anaconda'},
    {'id': 3, 'name' : 'Lets learn swing'},

]
# Create your views here.
def home (request):
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request):
    return render(request, 'room.html')

