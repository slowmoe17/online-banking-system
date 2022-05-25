from rest_framework import generics, permissions 
from users.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Transaction, BankAccount
from .serializers import  TransactionSerializer

class Transfer(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        try:
            sender = request.data['sender']
            receiver = request.data['receiver']
            amount = request.data['amount']
            sender_account = BankAccount.objects.get(account_number=sender)
            receiver_account = BankAccount.objects.get(account_number=receiver)
            if sender_account.balance < int(amount):
                return Response({"error": "Insufficient funds"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                sender_account.balance -= int(amount)
                receiver_account.balance += int(amount)
                sender_account.save()
                receiver_account.save()
                transaction = Transaction(sender=sender_account, receiver=receiver_account, amount=amount)
                transaction.save()
                return Response({"data": "Transfer successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# class that get all the transactions of a user
class GetTransactions(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, account_number):
        try:
            account = BankAccount.objects.get(account_number=BankAccount.account_number, user=request.user)
            transactions = Transaction.objects.filter(sender=account, receiver=account_number)
            serializer = TransactionSerializer(transactions, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


