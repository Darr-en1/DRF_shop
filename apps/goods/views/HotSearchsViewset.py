from rest_framework import mixins, viewsets

from goods.models import HotSearchWords
from goods.serializers.HotWordsSeriaizer import HotWordsSeriaizer


class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by('-index')
    serializer_class = HotWordsSeriaizer
