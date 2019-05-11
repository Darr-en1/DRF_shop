from rest_framework import serializers

from goods.models import GoodsCategory


class GoodCategoryModelSerializer(serializers.ModelSerializer):
    """
    常规序列化
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"
