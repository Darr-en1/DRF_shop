from rest_framework import serializers

from apps.goods.models import GoodsCategory


class GoodCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"
