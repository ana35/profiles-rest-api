from rest_framework import serializers  #imports all the different types of
                                        #serializers that we can use with
                                       #django rest framework.
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta: #tells djangorestframework what all fields we want to take
                #from models.
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs =  {'password': {'write_only': True}}
        #tell djangorestframework what special attributes that we wanna
        #apply to these fields.

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
                email = validated_data['email'],
                name = validated_data['name']
            )

        user.set_password = validated_data['password']
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
