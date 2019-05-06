from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from goods.filters import GoodsListFilter
from goods.models import Goods
from goods.serializers.GoodsModelSerializer import GoodsModelSerializer


class GoodsModelViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsModelSerializer
    queryset = Goods.objects.all()
    # pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsListFilter
    search_fields = ('^name', 'shop_price', 'goods_desc')  # support  '^' '=' '@' '$'
    ordering_fields = ('name', 'parent_category')
    ordering = ('name',)  # default
