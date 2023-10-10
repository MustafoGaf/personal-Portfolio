from django.shortcuts import render, redirect
from .models import Room, Message
from .form import MessageForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
users = User.objects.all()

def chat(req):
    return render(req, 'Chat/chat.html', {"users":users, "user_select":True})


def room(request, room):
        
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    if request.method == "POST":
        form = MessageForm()
        if form.is_valid:
            new_message = form.save(commit=False)
            new_message.save()
            new_message = ''
        
            request.POST = None
            return render(request, 'Chat/chat.html', {
            'username': username,
            'room': room,
            'room_details': room_details,
            'users':users, 
            'chat':True, "user_select":False, 'FormData':form})
        
    elif request.method == "GET":
        
        return render(request, 'Chat/chat.html', {
            'username': username,
            'room': room,
            'room_details': room_details,
            'users':users, 
            'chat':True, "user_select":False
        })
        
def setMessages(req, data):
    
    form = MessageForm(data=req.POST)
    if form.is_valid:
        new_message = form.save(commit=False)
        new_message.save()
        
        
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    r1 = room.split('|')
    r1.reverse()
    r1 = '|'.join(r1)
    if Room.objects.filter(name=room).exists():
        return redirect(''+room+'/?username='+username+'#footer')
    elif Room.objects.filter(name=r1).exists():
        return redirect(''+r1+'/?username='+username+'#footer')
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect(''+room+'/?username='+username+'#footer')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})