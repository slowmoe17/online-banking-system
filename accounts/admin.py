from django.contrib import admin
from .models import Transaction, BankAccount
admin.site.site_header = "Banking Admin"
admin.site.site_title = "Banking Admin Portal"
admin.site.index_title = "Welcome to Banking Portal"
admin.site.register(Transaction)
admin.site.register(BankAccount)
