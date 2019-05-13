from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user_operation.models import UserFav
from user_operation.serializers.UserFavDetailSerializer import UserFavDetailSerializer
from user_operation.serializers.UserFavSerializer import UserFavSerializer
from utils.permissions import IsOwnerOrReadOnly


class UserFavViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    # queryset = UserFav.objects.all()
    # 重写GenericViewSet.get_queryset保证只能操作当前用户收藏
    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # 应用于执行单个模型实例的对象查找的模型字段。默认为'pk'，在GenericAPIView定义的类变量，通过lookup_field可以覆盖
    lookup_field = 'goods_id'

    # IsAuthenticated 用户书否登陆    https://www.django-rest-framework.org/api-guide/permissions/#isauthenticated
    # IsOwnerOrReadOnly 自定义权限，只能删除用户自己的收藏
    # https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    # 使用jwt或则用户名密码验证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # serializer_class = UserFavSerializer

    # 动态设置Serializer,serializer_class可以不用了
    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavDetailSerializer
        elif self.action == 'create':
            return UserFavSerializer
        return UserFavSerializer
