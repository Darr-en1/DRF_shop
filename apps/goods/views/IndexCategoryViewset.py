from rest_framework import mixins, viewsets

from goods.models import GoodsCategory
from goods.serializers.IndexCategorySerializer import IndexCategorySerializer


class IndexCategoryViewset(mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    '''
    首页商品分类数据
    '''
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=['生鲜食品', '酒水饮料'])
    serializer_class = IndexCategorySerializer
