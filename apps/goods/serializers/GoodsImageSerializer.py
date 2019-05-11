from rest_framework import serializers

from goods.models import GoodsImage


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)
