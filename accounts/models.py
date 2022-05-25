from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from users.models import User

class Transaction(models.Model):
    amount = models.IntegerField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} {} {}'.format(self.sender, self.receiver, self.amount)
    

class BankAccount(models.Model):
    AccountTypes = (
        ('Savings', 'Savings'),
        ('Current', 'Current'),
    )
    AccountStatus = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.IntegerField(default=0)
    account_type = models.CharField(max_length=20,choices=AccountTypes, default='Savings')
    status = models.CharField(max_length=20, default='active', choices=AccountStatus)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.account_number + ' ' + self.user.username

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValueError('Balance cannot be negative')
        else:
            super(BankAccount, self).save(*args, **kwargs)
        
    def balance_change(self, amount):
        if self.status == 'Inactive':
            raise ValueError('Account is inactive')
        else:
            self.balance += amount
            self.save()
            return self.balance

    
