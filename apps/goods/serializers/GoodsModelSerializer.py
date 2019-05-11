from rest_framework import serializers

from goods.models import Goods
from goods.serializers.GoodCategoryModelSerializer import GoodCategoryModelSerializer
from goods.serializers.GoodCategoryNestModelSerializer import GoodCategoryNestModelSerializer
from goods.serializers.GoodsImageSerializer import GoodsImageSerializer


class GoodsModelSerializer(serializers.ModelSerializer):
    category = GoodCategoryNestModelSerializer()
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"
