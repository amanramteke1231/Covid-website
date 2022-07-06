from unittest import result
from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    
    result = None
    Global = None
    Countries = None
    data = True
    while(data):

        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()
            Global = json['Global']
            Countries = json['Countries']
            contaxt = {
            'Global': Global,
            'Countries': Countries
        }
            data = False
        except:
            data = True
    return render(request, 'home.html', contaxt)