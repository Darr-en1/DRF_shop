from rest_framework import mixins
from rest_framework import viewsets

from apps.goods.models import GoodsCategory
from apps.goods.serializers.GoodCategoryModelSerializer import GoodCategoryModelSerializer


class GoodCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodCategoryModelSerializer
