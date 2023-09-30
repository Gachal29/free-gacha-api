from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .gacha import Gacha
from .validators import GachalAPIValidator


class GachalAPI(APIView):
    def post(self, request):
        validator = GachalAPIValidator(data=request.data)
        validated_data = validator.validate()
        if validated_data["data"]:
            gacha = Gacha(validated_data["data"])
            result = {"result": gacha.gachal()}
        else:
            raise ValidationError(validated_data["error"])
        return Response(result)
