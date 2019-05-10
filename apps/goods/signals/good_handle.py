from django.db.models.signals import post_save
from django.dispatch import receiver

from goods import models


@receiver(post_save, sender=models.Goods)
def create_enrolled_record(sender, instance=None, created=False, **kwargs):
    """
    :param sender:
    :param instance:保存后的对象
    :param created: 是否是创建新的记录
    :param kwargs:
    :return:
    """
    if created:
        print(instance.__dict__)

    pass
