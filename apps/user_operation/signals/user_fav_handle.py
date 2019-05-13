from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from user_operation import models


@receiver(post_save, sender=models.UserFav)
def create_enrolled_record(sender, instance=None, created=False, **kwargs):
    """
    :param sender:
    :param instance:保存后的对象
    :param created: 是否是创建新的记录
    :param kwargs:
    :return:
    """
    if created:
        # Userfav中的goods 找 goods做增量
        goods = instance.goods
        goods.fav_num += 1
        goods.save()


@receiver(post_delete, sender=models.UserFav)
def delete_enrolled_record(sender, instance=None, created=False, **kwargs):
    """
    :param sender:
    :param instance:保存后的对象
    :param created: 是否是创建新的记录
    :param kwargs:
    :return:
    """
    if not created:
        goods = instance.goods
        goods.fav_num -= 1
        goods.save()
