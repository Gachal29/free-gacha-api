import random


class Gacha:
    def __init__(self, data):
        self.contents = data["contents"]
        self.extraction_num = data["extraction_num"]
        self.same = data["same"]

        if self.same:
            self.weights = data["weights"]

    def gachal(self):
        if self.same:
            result = random.choices(
                self.contents, k=self.extraction_num, weights=self.weights
            )
        else:
            result = random.sample(self.contents, k=self.extraction_num)
        return result
