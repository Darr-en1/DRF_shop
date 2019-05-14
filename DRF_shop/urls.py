"""DRF_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from DRF_shop import settings
from apps.users.views.SmsCodeViewSet import SmsCodeViewset
from goods.views.BannerViewset import BannerViewset
from goods.views.GoodCategoryNestViewSet import GoodCategoryNestViewSet
from goods.views.GoodCategoryViewSet import GoodCategoryViewSet
from goods.views.GoodsApiView import GoodsListApiView
from goods.views.GoodsModelViewSet import GoodsModelViewSet
from goods.views.HotSearchsViewset import HotSearchsViewset
from goods.views.IndexCategoryViewset import IndexCategoryViewset
from trade.views.OrderViewset import OrderViewset
from trade.views.ShoppingCartViewset import ShoppingCartViewset
from user_operation.views.AddressViewset import AddressViewset
from user_operation.views.LeavingMessageViewset import LeavingMessageViewset
from user_operation.views.UserFavViewSet import UserFavViewSet
from users.views.UserViewSet import UserViewSet

router = DefaultRouter()
"==============================apps.goods========================================"
router.register(r'goods', GoodsModelViewSet, base_name='goods')

router.register(r'good_category', GoodCategoryViewSet, base_name='good_category')

router.register(r'good_nest_category', GoodCategoryNestViewSet, base_name='good_nest_category')

router.register(r'code', SmsCodeViewset, base_name='code')

router.register(r'banner', BannerViewset, base_name='banner')

router.register(r'hot_search', HotSearchsViewset, base_name='hot_search')

router.register(r'index_category', IndexCategoryViewset, base_name='index_category')

"==============================apps.user_operation========================================"
router.register(r'user_fav', UserFavViewSet, base_name='user_fav')

router.register(r'user_leaving_message', LeavingMessageViewset, base_name='user_leaving_message')

router.register(r'user_address', AddressViewset, base_name='user_address')
"==============================apps.users========================================"
router.register(r'users', UserViewSet, base_name='users')

"==============================apps.trade========================================"
router.register(r'shopping_cart', ShoppingCartViewset, base_name='shopping_cart')

router.register(r'orders', OrderViewset, base_name='orders')
urlpatterns = [

                  path('xadmin/', xadmin.site.urls),
                  path('schema/', get_schema_view(title='DRF_Shop')),

                  # drf自带的Token
                  path('api-token-auth/', views.obtain_auth_token),

                  # JWT认证接口
                  path('jwt-auth/', obtain_jwt_token),

                  path('', include(router.urls)),

                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                  path('docs/', include_docs_urls(title='VUE_DRF_Shop')),

                  path('good_list/', GoodsListApiView.as_view(), name="good_list")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
