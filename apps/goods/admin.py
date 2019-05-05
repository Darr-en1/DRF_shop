from django.contrib import admin

# Register your models here.
from goods.models import Goods, GoodsCategory, GoodsCategoryBrand, GoodsImage, IndexAd, Banner, HotSearchWords

admin.site.register(Goods)
admin.site.register(GoodsCategory)
admin.site.register(GoodsCategoryBrand)
admin.site.register(GoodsImage)
admin.site.register(IndexAd)
admin.site.register(Banner)
admin.site.register(HotSearchWords)
