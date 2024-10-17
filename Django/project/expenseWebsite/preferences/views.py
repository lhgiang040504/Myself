from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import Preferences
from django.contrib import messages
# Create your views here.
"""
import pdb
pdb.set_trace()
"""

def index(request):

    currency_data = []
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for k, v in data.items():
            currency_data.append({'name': k, 'value': v})
    
    exists = Preferences.objects.filter(user=request.user).exists()
    user_preferences = None

    if exists:
        user_preferences = Preferences.objects.get(user=request.user)
    if request.method == 'GET':
        return render(request, 'index_preferences.html', {'currencies': currency_data, 'user_preferences': user_preferences})
    else:

        currency = request.POST['currency']
        if exists:
            user_preferences.currency = currency
            user_preferences.save()
        else:
            Preferences.objects.create(user=request.user, currency=currency)
        
        messages.success(request, 'Changes saved')
        return render(request, 'index_preferences.html', {'currencies': currency_data, 'user_preferences': user_preferences})