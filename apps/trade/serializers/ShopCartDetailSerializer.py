from rest_framework import serializers

from goods.serializers.GoodsModelSerializer import GoodsModelSerializer
from trade.models import ShoppingCart


class ShopCartDetailSerializer(serializers.ModelSerializer):
    # 一条购物车关系记录对应的只有一个goods。
    goods = GoodsModelSerializer(many=False, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ("goods", "nums")

