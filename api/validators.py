from .error_messages import (
    API_ERROR_DATA_FORMAT,
    API_ERROR_NO_CONTENTS,
    API_ERROR_OVER_EXTRACTION_NUM,
    API_ERROR_SAME_CONSTRAIN,
)


class GachalAPIValidator:
    def __init__(self, **kwargs):
        self.data = kwargs["data"]
        self.validated_data = {"data": None, "error": None}

    def validate(self):
        if type(self.data) is not dict:
            self.validated_data["error"] = {
                "detail": API_ERROR_DATA_FORMAT.format("Request Content", "dict")
            }
            return self.validated_data

        contents = self.data.get("contents", None)
        if type(contents) is not list:
            self.validated_data["error"] = {
                "detail": API_ERROR_DATA_FORMAT.format("contents", "list")
            }
            return self.validated_data
        if not contents:
            self.validated_data["error"] = {"detail": API_ERROR_NO_CONTENTS}
            return self.validated_data

        same = self.data.get("same", False)
        extraction_num = self.data.get("extraction_num", None)
        if same:
            if type(same) is not bool:
                self.validated_data["error"] = {
                    "detail": API_ERROR_DATA_FORMAT.format("same", "boolean")
                }
                return self.validated_data

            if not extraction_num:
                self.validated_data["error"] = {"detail": API_ERROR_SAME_CONSTRAIN}
                return self.validated_data
        else:
            if not extraction_num:
                extraction_num = len(contents)

            if extraction_num > len(contents):
                self.validated_data["error"] = {"detail": API_ERROR_OVER_EXTRACTION_NUM}
                return self.validated_data

        if type(extraction_num) is not int:
            self.validated_data["error"] = {
                "detail": API_ERROR_DATA_FORMAT.format("extraction_num", "int")
            }
            return self.validated_data

        if extraction_num == 1:
            same = False

        weights = []
        if same and type(contents) is not dict:
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
