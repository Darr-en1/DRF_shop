from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from user_operation.models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    # HiddenField的值不依靠输入，而需要设置默认的值，不需要用户自己post数据过来，
    # 也不会显式返回给用户，最常用的就是user!    需要保证本用户只能操作自己进行操作
    # https://www.django-rest-framework.org/api-guide/validators/#currentuserdefault
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav

        # 使用validate方式实现唯一联合(一个user对goods的收藏只能一次)
        # https://www.django-rest-framework.org/api-guide/validators/#uniquetogethervalidator
        validators = [
            UniqueTogetherValidator(  # 数据库需要对字段做联合索引，在model 的Meta中，因此需要migrations
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]

        fields = ('user', 'goods', 'id')
