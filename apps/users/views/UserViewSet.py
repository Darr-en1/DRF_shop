from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler

from users.serializers.UserDetailSerializer import UserDetailSerializer
from users.serializers.UserRegModelSerializer import UserRegModelSerializer

# from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

User = get_user_model()


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    # serializer_class = UserRegModelSerializer

    # 动态设置Serializer,因此serializer_class可以不用
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegModelSerializer
        return UserDetailSerializer

    # queryset = User.objects.all()

    # 通过重写，返回当前用户，不用走get_queryset()  ,queryset可以不用
    def get_object(self):
        return self.request.user

    # 添加认证方式
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # 这样会导致用户注册也需要登陆验证，可以重新定义一个class或者设置动态设置权限认证
    # permission_classes = (IsAuthenticated,)
    # 动态设置permission(extends 权限设置的function,对于用户详情展示设置权限)
    # 继承APIView 的get_permissions
    def get_permissions(self):
        if self.action == 'retrieve':
            return [IsAuthenticated()]
        elif self.action == 'create':
            return []
        return []

    def create(self, request, *args, **kwargs):
        '''
        注册完成之后登陆
        获取JWT  token 设置到api中
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 获取当前创建的User对象
        user = self.perform_create(serializer)
        # api返回的数据
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        '''
        :param serializer:  User序列化对象
        :return:  返回创建的User对象
        '''
        return serializer.save()
