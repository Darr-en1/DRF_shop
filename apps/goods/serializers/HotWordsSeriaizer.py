from rest_framework import serializers

from goods.models import HotSearchWords


class HotWordsSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"
