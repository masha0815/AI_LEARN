from django.shortcuts import render
from django.http import

# Create your views here.
def index(request) :
    return render(request, 'topic/index.html')

def add_topic(request) :
    return render(request, 'topic/add_topic.html')


