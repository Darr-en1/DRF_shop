from rest_framework import serializers

from goods.models import Goods
from trade.models import ShoppingCart
from user_operation.models import UserLeavingMessage


class ShopCartSerializer(serializers.Serializer):
    # 使用Serializer本身最好, 因为它是灵活性最高的。
    # unique_together = ("user", "goods")
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    nums = serializers.IntegerField(required=True, label="数量", min_value=1,
                                    error_messages={
                                        "min_value": "商品数量不能小于一",
                                        "required": "请选择购买数量"
                                    })
    # https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    def create(self, validated_data):
        user = self.context["request"].user
        nums = validated_data["nums"]
        goods = validated_data["goods"]

        existed = ShoppingCart.objects.filter(user=user, goods=goods)

        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    # Serializer继承于baseSerializer。但是Serializer并没有去重写update方法。
    def update(self, instance, validated_data):
        # 修改商品数量
        instance.nums = validated_data["nums"]
        instance.save()
        return instance
