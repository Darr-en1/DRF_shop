from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import Goods
from goods.serializers.GoodsModelSerializer import GoodsModelSerializer


class GoodsListApiView(APIView):
    def get(self, request, *args, **kwargs):
        goods = Goods.objects.all()[:10]
        serializer = GoodsModelSerializer(goods, many=True)
        return Response(serializer.data)
