from rest_framework.response import Response
from rest_framework.views import APIView

from .gacha import Gacha
from .validators import GachalAPIValidator


class GachalAPI(APIView):
    def post(self, request):
        validator = GachalAPIValidator(data=request.data)
        validated_data = validator.validate()
        gacha = Gacha(validated_data.get("data", {}))
        result = {"result": gacha.gachal()}
        return Response(result)
