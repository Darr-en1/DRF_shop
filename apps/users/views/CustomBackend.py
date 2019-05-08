from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证规则


    """

    def authenticate(self, username=None, password=None, **kwargs):
        """
            Django 默认是 username password ,但是如果是手机登陆就需要自己重写  需要在setting指定
        :param username:
        :param password:
        :param kwargs:
        :return:
        """
        try:
            # 不希望用户存在两个，get只能有一个.两个是get失败的一种原因
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            # django的后台中密码加密：所以不能password==password  UserProfile继承的AbstractUser中有def check_password(self,raw_password):
            if user.check_password(password):
                return user
        except Exception:
            return None
