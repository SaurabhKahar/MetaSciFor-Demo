from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Default Name')
    surname = models.CharField(max_length=100, default='Default Surname')
    email = models.EmailField(default='default@example.com')
    age = models.IntegerField(default=0)  # Provide a sensible default
    contact_number = models.CharField(max_length=15, default='000-000-0000')

    def __str__(self):
        return self.user.username

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.source} - {self.amount}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.source} - {self.amount}"

    
