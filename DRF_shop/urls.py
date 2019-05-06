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
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from DRF_shop import settings
from goods.views.GoodCategoryNestViewSet import GoodCategoryNestViewSet
from goods.views.GoodCategoryViewSet import GoodCategoryViewSet
from goods.views.GoodsApiView import GoodsListApiView
from goods.views.GoodsModelViewSet import GoodsModelViewSet

router = DefaultRouter()
router.register(r'goods', GoodsModelViewSet, base_name='goods')
router.register(r'good_category', GoodCategoryViewSet, base_name='good_category')
router.register(r'good_nest_category', GoodCategoryNestViewSet, base_name='good_nest_category')

urlpatterns = [
                  path('admin/', admin.site.urls),

                  path('', include(router.urls)),

                  path('docs/', include_docs_urls(title='VUE_DRF_Shop')),

                  path('good_list/', GoodsListApiView.as_view(), name="good_list")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
