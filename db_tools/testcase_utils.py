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

        GoodsCategory.objects.create(
            name=f"test_category{category_number + 1}",
            desc=f"test_category{category_number + 1}_desc",
            category_type=random.randint(1, 3),
            parent_category=goods_category_obj
        )

        return goods_category_obj
