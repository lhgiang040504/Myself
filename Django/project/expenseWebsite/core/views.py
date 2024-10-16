from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    return render(request, 'index.html')

def add_expense(request):
    return render(request, 'add_expense.html')