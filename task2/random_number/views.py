from django.shortcuts import render
from django.http import HttpResponse
import random

def random_number(request):
    num = random.randint(0,100)
    html = "Random Number: %s" % num
    return HttpResponse(html)

# Create your views here.
