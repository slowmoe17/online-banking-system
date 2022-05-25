from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import BankAccount
from django.contrib.auth.models import User
import random



def generate_account_number():
    account_number = ''
    for i in range(12):
        account_number += str(random.randint(0, 9))
    return account_number

@receiver(post_save, sender=User)
def create_bank_account(sender, instance, created, **kwargs):
    if created:
        BankAccount.objects.create(user=instance, account_number=generate_account_number(), balance=0)
