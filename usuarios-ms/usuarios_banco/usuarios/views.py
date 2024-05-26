from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Account, Transaction
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard.html')
    return render(request, 'usuarios/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def dashboard(request):
    account = Account.objects.get(user=request.user)
    transactions = Transaction.objects.filter(account=account).order_by('-timestamp')
    return render(request, 'usuarios/dashboard.html', {'account': account, 'transactions': transactions})

@login_required
def deposit(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        account = Account.objects.get(user=request.user)
        account.balance += amount
        account.save()
        Transaction.objects.create(account=account, amount=amount, description='Deposit')
        return redirect('dashboard')
    return render(request, 'usuarios/deposit.html')

@login_required
def withdraw(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        account = Account.objects.get(user=request.user)
        if account.balance >= amount:
            account.balance -= amount
            account.save()
            Transaction.objects.create(account=account, amount=-amount, description='Withdrawal')
            return redirect('dashboard')
        else:
            return render(request, 'usuarios/withdraw.html', {'error': 'Insufficient balance'})
    return render(request, 'usuarios/withdraw.html')
