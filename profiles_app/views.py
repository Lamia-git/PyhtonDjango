from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import authentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_app import persmissions
from profiles_app import serializers
from profiles_app import models

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
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_methode':'GET'})

    def update(self, request, pk=None):
        """handle updating an object by its ID"""
        return Response({'http_methode':'PUT'})

    def partial_update(self, request, pk=None):
        """handle partial updating an object by its ID"""
        return Response({'http_methode':'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing object"""
        return Response({'http_methode':'DELETE'})


class userProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfilesSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (persmissions.UpdateOwnProfile,)
    filter_backends =(filters.SearchFilter,)
    search_fields = ('name','email')
    

class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentification tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES