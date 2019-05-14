from django.db.models import Q
from rest_framework import serializers

from goods.models import GoodsCategoryBrand, IndexAd, Goods, GoodsCategory
from goods.serializers.GoodCategoryNestModelSerializer import CategorySerializer2
from goods.serializers.GoodsModelSerializer import GoodsModelSerializer


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"


class IndexCategorySerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True)
    # https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    goods = serializers.SerializerMethodField()
    # 获取二级商品分类
    sub_cat = CategorySerializer2(many=True)

    ad_goods = serializers.SerializerMethodField()

    def get_ad_goods(self, obj):
        goods_json = {}
        ad_goods = IndexAd.objects.filter(category_id=obj.id, )
        if ad_goods:
            good_ins = ad_goods[0].goods
            goods_json = GoodsModelSerializer(good_ins, many=False, context={'request': self.context['request']}).data
        return goods_json

    def get_goods(self, obj):
        # 将这个商品相关父类子类等都可以进行匹配
        all_goods = Goods.objects.filter(Q(category_id=obj.id) | Q(category__parent_category_id=obj.id) | Q(
            category__parent_category__parent_category_id=obj.id))
        # 获取good数据   context={'request': self.context['request']}
        # 嵌套 serializer img会判断上下文是否存在request，存在地址就会带上域名
        goods_serializer = GoodsModelSerializer(all_goods, many=True, context={'request': self.context['request']})
        return goods_serializer.data

    class Meta:
        model = GoodsCategory
        fields = "__all__"
