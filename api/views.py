from django.shortcuts import render, redirect
from urllib.request import urlopen
from django.contrib import messages
import json

from .utils import (
    login, 
    own_details, 
    get_applicable_share,
    apply_share
)
from .models import Info

# Create your views here.
def dashboard(request):
    users = Info.objects.all()
    
    userDetails = []
    for user in users:
        token = login(user).strip()
        userDetails.append(own_details(token))
    return render(request, 'api/dashboard.html', { "users": users, "userDetails": userDetails })

def add_account(request):
    res = urlopen('https://webbackend.cdsc.com.np/api/meroShare/capital/')
    capitals = json.loads(res.read())
    return render(request, 'api/add.html', { "capitals": capitals })

def save(request):
    if request.method == 'POST':
        clientId = request.POST['clientId']
        username = request.POST['username']
        password = request.POST['password']
        crn = request.POST['crn']
        pin = request.POST['pin']

        info = Info(
            clientId=clientId,
            username=username,
            password=password,
            crn=crn,
            pin=pin
        )
        info.save()
        messages.success(request, 'Date has been successfully saved!')

    return redirect('dashboard')

def batch_apply(request):
    users = Info.objects.all()

    if request.method == 'POST':
        kittas = request.POST['kittas']
        selectedIpo = request.POST['selectedIpo']

        messages = apply_share(users, kittas, selectedIpo)

    return render(request, 'api/batch_apply.html', { "users": users, "response": messages })

def user_input(request):
    user = Info.objects.first()

    if user:
        token = login(user)
        applicableIpos = get_applicable_share(token)['object']
    else:
        applicableIpos = None
    return render(request, 'api/user_input.html', { "applicableIpos": applicableIpos })

def about(request):
    return render(request, 'api/about.html')

def contact(request):
    return render(request, 'api/contact.html')