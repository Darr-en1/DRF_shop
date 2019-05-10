from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
# from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

# from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler

from users.serializers.UserRegModelSerializer import UserRegModelSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserRegModelSerializer

    # # 动态设置Serializer
    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return USerDetailSerializer
    #     elif self.action == 'create':
    #         return UserRegSerializer
    #     return USerDetailSerializer
    #
    # # queryset = User.objects.all()
    #
    # # 这样会导致用户注册也需要登陆验证，可以重新定义一个class或者设置动态设置权限认证
    # # permission_classes = (IsAuthenticated,)
    #
    # # 使用jwt验证后，用户登陆不能获取权限，需加入SessionAuthentication的认证
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    #
    # # 动态设置permission(extends 权限设置的function,对于用户详情展示设置权限)
    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return [IsAuthenticated()]
    #     elif self.action == 'create':
    #         return []
    #     return []
    #
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
    #
    # # 返回当前用户
    # def get_object(self):
    #     return self.request.user
