from rest_framework import serializers

from goods.models import GoodsCategory


class GoodCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"
