# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from db_tools.testcase_utils import TestTool
from goods.models import GoodsCategory


class TestGetGoodNestCategory(APITestCase):
    fixtures = ['goods_data.json']

    def setUp(self):
        self.goods_category_obj = TestTool.test_create_category(1)

    def test_get_good_nest_category(self):
        # 对于DRF router 注册的api  base_name + -detail or -list表明请求类别，通过kwargs，args传参
        # response = self.client.get(reverse('good_nest_category-detail', kwargs={'pk': self.goods_category_obj.id}))
        response = self.client.get(reverse('good_nest_category-detail', args=(self.goods_category_obj.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_good_nest_category_list(self):
        response = self.client.get(reverse('good_nest_category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
