from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from chat.models import Room

import string
import random


# Create your views here.
@login_required
def index(request, slug):
    room = Room.objects.get(slug=slug)
    context = {
        'name': room.name,
        'slug': room.slug
    }
    return render(request, 'chat/room.html', context)


@login_required
def room_create(request):
    if request.method == "POST":
        room_name = request.POST['room_name']
        uid = str(''.join(random.choices(string.ascii_letters + string.digits, k=4)))
        room_slug = slugify(room_name + "_" + uid)
        room = Room.objects.create(name=room_name, slug=room_slug)
        context = {
            'slug': room.slug
        }
        return redirect(reverse('chat', kwargs=context))
    else:
        return render(request, 'chat/create.html')


@login_required
def room_join(request):
    if request.method == "POST":
        room_slug = request.POST['room_slug']
        room = Room.objects.get(slug=room_slug)
        context = {
            'slug': room.slug
        }
        return redirect(reverse('chat', kwargs=context))
    else:
        return render(request, 'chat/join.html')
