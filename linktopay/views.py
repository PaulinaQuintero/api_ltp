from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from  .models import LinkToPayRequest
from .serializers import LinkToPaySerializer
# Create your views here.
# class LinkToPayViewSet(viewsets.ModelViewSet):
#     queryset = LinkToPayRequest.objects.all();
#     serializer_class = LinkToPaySerializer


class LinkToPayView(APIView):
    def get(self, request):
        links = LinkToPayRequest.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = LinkToPaySerializer(links, many=True)
        return Response({"links": serializer.data})

    def post(self, request):
        link = request.data.get('data')

        # Create an article from the above data
        serializer = LinkToPaySerializer(data=link)
        if serializer.is_valid(raise_exception=True):
            link_saved = serializer.save()
        return Response({"success": "Link '{}' created successfully".format(link_saved)})




# class LinkToPayView(APIView):
#     @api_view(['GET', 'POST'])
#     def link_list(request):
#         """
#         List all code snippets, or create a new snippet.
#         """
#         if request.method == 'GET':
#             links =LinkToPayRequest.objects.all()
#             serializer = LinkToPaySerializer(links, many=True)
#             return Response(serializer.data)
#
#         elif request.method == 'POST':
#             serializer = LinkToPaySerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








