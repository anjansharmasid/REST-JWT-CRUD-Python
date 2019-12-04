from django.shortcuts import render
from rest_framework import  viewsets, permissions
from . models import Customer
from .serialzers import CustomerSerializer
# Create your views here.

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    #permissions_class = (permissions.IsAuthenticatedOrReadOnly,)

