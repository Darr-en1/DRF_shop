from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    '''
    用户详情序列化
    '''

    class Meta:
        model = User
        fields = ('name', 'birthday', 'gender', 'mobile', 'email')
