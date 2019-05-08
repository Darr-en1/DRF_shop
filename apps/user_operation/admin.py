from django.contrib import admin

# Register your models here.
from apps.user_operation.models import UserFav, UserLeavingMessage, UserAddress

admin.site.register(UserFav)
admin.site.register(UserLeavingMessage)
admin.site.register(UserAddress)
