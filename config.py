import json


class Config:
    def getDataFileJson(self, filename: str):
        with open(filename, encoding="utf-8") as file:
            data = json.loads(file.read())
            file.close()
            return data
    def writeDataFileJson(self, filename: str, data: dict={}):
        with open(filename, "w+", encoding="utf-8") as file:
            json.dump(data, file)
            file.close()
