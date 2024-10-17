from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('login')  # Redirect to login page

def add_expense(request):
    return render(request, 'add_expense.html')