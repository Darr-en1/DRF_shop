from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from users.models import VerifyCode
from users.serializers.SmsSerializer import SmsSerializer


class SmsCodeViewset(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            from random import choice
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]

        # yun_pian = YunPian(APIKEY)

        code = self.generate_code()

        # sms_status = yun_pian.send_sms(code=code, mobile=mobile)

        # if sms_status["code"] != 0:
        #     return Response({
        #         "mobile":sms_status["msg"]
        #     }, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     code_record = verifyCode(code=code, mobile=mobile)
        #     code_record.save()
        #     return Response({
        #         "mobile":mobile
        #     }, status=status.HTTP_201_CREATED)

        # 模拟
        code_record = VerifyCode(code=code, mobile=mobile)
        code_record.save()
        return Response({
            'mobile': mobile
        }, status=status.HTTP_201_CREATED)
