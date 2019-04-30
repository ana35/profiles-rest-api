from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #contains a list of different http statuses.
from . import serializers

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API View features"""

        an_APIView = [
                'Uses HTTP methods as functions (get, post, patch, put, delete)',
                'Is similar to a traditional Django View',
                'Gives you the most control over your logic',
                'Is mapped manually to URLs',
            ]

        return Response({'message' : 'Hello', "an_apiview" : an_APIView})

    def post(self, request):
        """Creates a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})

        else:
            return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return Response({'method' : 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request."""

        return Response({'method' : 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method' : 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
                'uses actions (list, create, view, update, partial update)',
                'automatically maps to urls using Routers',
                'provides more functionality with less code.'
            ]

        return Response({'message' : 'hello', 'a_viewset': a_viewset})
