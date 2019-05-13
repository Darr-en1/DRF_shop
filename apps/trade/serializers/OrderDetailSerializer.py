from rest_framework import serializers

from goods.serializers.GoodsModelSerializer import GoodsModelSerializer
from trade.models import OrderGoods, OrderInfo


class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsModelSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = "__all__"
