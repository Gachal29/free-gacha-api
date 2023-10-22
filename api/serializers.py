from rest_framework import serializers
from rest_framework.serializers import ValidationError


class GachalSerializer(serializers.Serializer):
    contents = serializers.ListField()
    same = serializers.BooleanField(default=False)
    extraction_num = serializers.IntegerField(required=False)
    weights = serializers.ListField(required=False)

    def validate(self, data):
        # extraction_numとweights周り
        if data["same"]:
            # extraction_num
            if not "extraction_num" in data:
                raise ValidationError("'same'がtrueの際は、'extraction_num'は必須です。")
            if data["extraction_num"] == 1:
                data["same"] = False
            
            # weights
            if not "weights" in data:
                data["weights"] = [1] * len(data["contents"])
            else:
                if len(data["contents"]) in len(data["weights"]):
                    raise ValidationError("'content'と'weights'の個数が一致しません。")
        else:
            # extraction_num
            if not "extraction_num" in data:
                data["extraction_num"] = len(data["contents"])
            else:
                if data["extraction_num"] > len(data["contents"]):
                    raise ValidationError("sameがfalseの際は、'extraction_num'は'contents'の要素数以下に設定してください。")
        return data
    
    def validate_contents(self, contents):
        # contentsの存在を確認
        if len(contents) == 0:
            raise ValidationError("'contents'がありません。")
        return contents
