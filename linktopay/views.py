from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from  .models import LinkToPayRequest
from .serializers import LinkToPaySerializer
# Create your views here.
class LinkToPayViewSet(viewsets.ModelViewSet):
    queryset = LinkToPayRequest.objects.all();
    serializer_class = LinkToPaySerializer








