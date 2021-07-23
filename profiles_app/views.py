from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_app import serializers


# Create your views here.


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a list of APIView Features"""

        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional Django view',
            'gives you the most control over you application logic',
            'is mapped manually to urls'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'methode': 'PUT'})

    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({'method': 'Patch'})


    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message':'DELETE'})