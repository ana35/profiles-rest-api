from rest_framework import serializers #imports all the different types of serializers that we can use with
                                       #django rest framework.

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)
