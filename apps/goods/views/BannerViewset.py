from rest_framework import mixins, viewsets

from goods.models import Banner
from goods.serializers.BannerSerializer import BannerSerializer


class BannerViewset(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    '''
    获取轮播图列表
    '''
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerializer