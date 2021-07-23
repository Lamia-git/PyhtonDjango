from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import Reponse


# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """return a list of APIView Features"""

        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional Django view',
            'gives you the most control over you application logic',
            'is mapped manually to urls'
        ]
        return Response({'message':'Hello!', 'an_apiview': an_apiview})
