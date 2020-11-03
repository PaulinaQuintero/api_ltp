from django.shortcuts import render
from rest_framework import viewsets
from  .models import LinkToPayRequest
from .serializers import LinkToPaySerializer
# Create your views here.
class LinkToPayViewSet(viewsets.ModelViewSet):
    serializer_class = LinkToPaySerializer
    queryset = LinkToPayRequest.objects.all()




