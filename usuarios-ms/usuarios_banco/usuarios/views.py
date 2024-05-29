from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


from .models import Account, Transaction


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard.html')
    return render(request, 'usuarios/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear una cuenta en MongoDB para el nuevo usuario
            account = Account(user=user, balance=0)
            account.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def dashboard(request):
    try:
        account = Account.objects.get(user=request.user)
    except Account.DoesNotExist:
        return render(request, 'error.html', {'message': 'Account does not exist'})

@login_required
def deposit(request):
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        account = Account.objects.get(user=request.user)
        Transaction(account=account, amount=amount, type='deposit').save()
        account.balance += amount
        account.save()
        return redirect('dashboard')
    return render(request, 'deposit.html')

@login_required
def withdraw(request):
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        account = Account.objects.get(user=request.user)
        if account.balance >= amount:
            Transaction(account=account, amount=amount, type='withdraw').save()
            account.balance -= amount
            account.save()
            return redirect('dashboard')
        else:
            return render(request, 'error.html', {'message': 'Insufficient balance'})
    return render(request, 'withdraw.html')