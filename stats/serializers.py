from rest_framework import serializers
from .models import Stats
from django.contrib.auth.models import User

# serializer is used to convert model (like our stats model) to JSON
# this is one job of the DRF (Django Rest Framework), so you don't have to write code to convert it
# serializer also checks if the data is valid before saving it to the database

class StatsSerializer(serializers.ModelSerializer):
    # class Meta is used to change behavior of the model serializer, 
    # like which model to use, which fields to include, ordering, etc.
    class Meta:
        # tells the serializer which model to use, which is the Stats (see models.py for what fields it has)
        model = Stats

        # this means all fields in the model will be serialized
        fields = "__all__" 

        # user is username, and should not be modified by user. But it'll still be displayed in response
        read_only_fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # since we are only allowing user to login or register using username and password
        # maybe add email if neceessary in future

        fields = ['username', 'password']

        # password should not be read, only written
        # you can send password in request (POST) but it won't show up in response (GET)
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

        # overrides the default User.create_user method so that passsword is hashed
        # meaning by default, the create method will simply pass the password as plain text
        # but "hashing password" means converting it to not make it readable - for security measures
    def create(self, validated_data):
        # this **validated_data is the fields (username and password)
        # so its same as passing (username="name", password="password") in the create_user method
        return User.objects.create_user(**validated_data)