from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

def login_request(request):

    username = request.POST['username']
    password = request.POST['password']
    next_page = request.POST['next']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            redirect_url = "{}?token={}" . format (next_page, user.token)
            return HttpResponseRedirect(redirect_url)
        else:
            pass
    else:
        # Return an 'invalid login' error message.
        pass
