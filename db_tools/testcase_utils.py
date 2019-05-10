# #  获取当前文件的路径，以及路径的父级文件夹名
# import os
# import sys
#
# pwd = os.path.dirname(os.path.realpath(__file__))
# # 将项目目录加入setting
# sys.path.append(pwd + "../")
# # manage.py中
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DRF_shop.settings")
#
# import django
#
# django.setup()

import random

from goods.models import GoodsCategory


class TestTool:

    @staticmethod
    def test_create_category(category_number: int, **kwargs):
        goods_category_obj = GoodsCategory.objects.create(
            name=f"test_category{category_number}",
            desc=f"test_category{category_number}_desc",
            category_type=random.randint(1, 3)
        )

        goods_category_obj1 = GoodsCategory.objects.create(
            name=f"test_category{category_number + 1}",
            desc=f"test_category{category_number + 1}_desc",
            category_type=random.randint(1, 3),
            parent_category=goods_category_obj  # 外键关联
            # sub_cat=goods_category_obj   # 反向外键关联会出错，因为无该字段
        )
        # goods_category_obj1.sub_cat.add(goods_category_obj)  # 一对多反向外键关联  参数arg(允许多个)
        # goods_category_obj1.parent_category.add(goods_category_obj)  # 外键关联会出错，因为NoneType mot have add()，多对多可以使用

        return goods_category_obj


if __name__ == '__main__':
    TestTool.test_create_category(1)
