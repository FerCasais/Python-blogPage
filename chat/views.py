from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })
@login_required
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if room == '' :
        return redirect ('/wrong_room')

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
@login_required
def send(request):
    message = request.POST['message']
    username = request.user
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def wrong_room(request):
    contexto = {
           
    }
    http_response = render(
        request=request,
        template_name="wrong_room.html",
        context=contexto,
    )
    return http_response