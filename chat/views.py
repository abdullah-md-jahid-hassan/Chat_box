from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def chat_room(request, name, room_name):
    return render(
        request,
        'room.html',
        {
            'name': name,
            'room_name': room_name
        })