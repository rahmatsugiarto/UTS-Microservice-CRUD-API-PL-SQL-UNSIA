from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        # field = ('id', 'mobile', 'fullname')
        # fields = '__all__'
        fields = ['id', 'name', 'gender', 'username', 'password', "token"]
