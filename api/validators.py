from rest_framework.exceptions import ValidationError

from .error_messages import ErroMessages


class GachalAPIValidator:
    validated_data = {"data": None}

    def __init__(self, **kwargs):
        self.data = kwargs["data"]

    def validate(self):
        if not isinstance(self.data, dict):
            raise ValidationError(
                ErroMessages.API_ERROR_DATA_FORMAT.format("Request Content", "dict")
            )

        contents = self.data.get("contents", None)
        if not isinstance(contents, list):
            raise ValidationError(
                ErroMessages.API_ERROR_DATA_FORMAT.format("contents", "list")
            )
        if not contents:
            raise ValidationError(
                ErroMessages.API_ERROR_NO_CONTENTS
            )

        same = self.data.get("same", False)
        extraction_num = self.data.get("extraction_num", None)
        if same:
            if not isinstance(same, bool):
                raise ValidationError(
                    ErroMessages.API_ERROR_DATA_FORMAT.format("same", "boolean")
                )

            if not extraction_num:
                return ValidationError(
                    ErroMessages.API_ERROR_SAME_CONSTRAIN
                )
        else:
            if not extraction_num:
                extraction_num = len(contents)

            if extraction_num > len(contents):
                raise ValidationError(
                    ErroMessages.API_ERROR_OVER_EXTRACTION_NUM
                )

        if not isinstance(extraction_num, int):
            raise ValidationError(
                ErroMessages.API_ERROR_DATA_FORMAT.format("extraction_num", "int")
            )

        if extraction_num == 1:
            same = False

        weights = []
        if same:
            if isinstance(contents[0], dict):
                new_contents = []
                for content in contents:
                    weights.append(content.get("weight", 1))
                    new_contents.append(content.get("name", None))
                contents = new_contents

        self.validated_data["data"] = {
            "contents": contents,
            "extraction_num": extraction_num,
            "same": same,
            "weights": weights,
        }
        return self.validated_data
