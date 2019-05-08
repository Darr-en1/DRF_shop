from rest_framework import viewsets, mixins

from apps.goods.models import GoodsCategory
from apps.goods.serializers.GoodCategoryNestModelSerializer import GoodCategoryNestModelSerializer


class GoodCategoryNestViewSet(viewsets.ReadOnlyModelViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.all()

    serializer_class = GoodCategoryNestModelSerializer
