from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .gacha import Gacha
from .serializers import GachalSerializer


class GachalAPI(APIView):
    def post(self, request):
        serializers = GachalSerializer(data=request.data)
        if not serializers.is_valid():
            raise ValidationError(serializers.errors)
        gacha = Gacha(serializers.validated_data)
        result = {"result": gacha.gachal()}
        return Response(result)
