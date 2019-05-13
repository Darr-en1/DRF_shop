from rest_framework import serializers

from goods.serializers.GoodsModelSerializer import GoodsModelSerializer
from user_operation.models import UserFav


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsModelSerializer()

    class Meta:
        model = UserFav
        fields = ('goods', 'id')

