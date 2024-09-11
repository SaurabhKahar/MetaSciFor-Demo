from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import IncomeForm, ExpenseForm
from .models import Income, Expense
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import logout


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create a new user with the form data
            user = form.save()
            return redirect('login')
    else:
        form = SignupForm()
    
    return render(request, 'tracker/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'tracker/login.html', {'form': form})

@login_required
def dashboard_view(request):
    # Fetch all incomes for the logged-in user
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    # Calculate total income and expenses
    total_income = sum(income.amount for income in incomes)
    total_expense = sum(expense.amount for expense in expenses)
    total_balance = total_income - total_expense

    context = {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'total_balance': total_balance,
    }

    return render(request, 'tracker/dashboard.html', context)

@login_required
def add_income_view(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user      # Associate expense with logged-in user
            income.save()
            return redirect('dashboard')    # Redirect to dashboard after saving
    else:
        form = IncomeForm()
    return render(request, 'tracker/add_income.html', {'form': form})

@login_required
def add_expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  
            expense.save()
            return redirect('dashboard')  
    else:
        form = ExpenseForm()
    
    return render(request, 'tracker/add_expense.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def custom_logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login or any other page