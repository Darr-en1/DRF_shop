from rest_framework import serializers

from goods.models import Goods


class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"
