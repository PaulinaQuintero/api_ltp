from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from  .models import LinkToPayRequest
from .serializers import LinkToPaySerializer
# Create your views here.
class LinkToPayViewSet(viewsets.ModelViewSet):
    queryset = LinkToPayRequest.objects.all()
    serializer_class = LinkToPaySerializer






