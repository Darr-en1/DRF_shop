import time

from rest_framework import serializers

from trade.models import OrderInfo


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    # 设置自读属性
    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    add_time = serializers.DateTimeField(read_only=True)

    def generate_order_sn(self):
        # 当前时间 + user_id + 随机数
        from random import Random
        random_ins = Random()
        order_sn = f"{time.strftime('%Y%m%d%H%M%S')}{self.context['request'].user.id}{random_ins.randint(10, 99)}"
        return order_sn

    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        model = OrderInfo
        fields = "__all__"
