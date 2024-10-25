from django.shortcuts import render
from .utils import *

def home(request):
    url = 'https://newsapi.org/v2/everything?q=(business OR geopolitics)&apiKey=71b37b7884c547dfa5fad39676d3b877'
    getnews(url)  # Fetch the latest articles every time the page is accessed
    articles = Articles.objects.all()  # Get all articles from the database
    return render(request, 'home.html', context={'articles': articles})
