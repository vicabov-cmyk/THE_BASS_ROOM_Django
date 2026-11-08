from django.shortcuts import render


def home(request):
    return render(request, 'bassroom/home.html')


def events(request):
    return render(request, 'bassroom/events.html')


def artists(request):
    return render(request, 'bassroom/artists.html')


def about(request):
    return render(request, 'bassroom/about.html')


def contacts(request):
    return render(request, 'bassroom/contacts.html')
