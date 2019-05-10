from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import VerifyCode

User = get_user_model()


class UserRegModelSerializer(serializers.ModelSerializer):
    """
     用户注册序列化
     """
    # write_only=True   序列化返回不会返回该字段
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, error_messages={
        "blank": "请输入验证码",
        "required": "请输入验证码",
        "max_length": "验证码格式错误",
        "min_length": "验证码格式错误"
    },
                                 label="验证码")

    username = serializers.CharField(label="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    password = serializers.CharField(style={'input_type': 'password'},  # 设置为秘文
                                     label="密码", write_only=True)

    # 重载create方法  还可以使用信号量的方法
    # def create(self, validated_data):
    #     user = super(UserRegSerializer, self).create(validated_data=validated_data)
    #     #对密码加密
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user


    def validated_code(self, code):
        # 验证码在数据库中是否存在，用户从前端post过来的值都会放入initial_data里面，排序(最新一条)。
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
        if verify_records:
            # 获取到最新一条
            last_record = verify_records[0]

            # 有效期为五分钟。
            five_mintes_ago = datetime.now() - timedelta(hours=10, minutes=5, seconds=0)
            if five_mintes_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("验证码错误")

        # 不加字段名的验证器作用于所有字段之上。attrs是字段 validate之后返回的总的dict

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username", "code", "password")
