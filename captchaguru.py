import requests
from io import BytesIO
import base64
import time
class CaptchaGuru:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
    def createJob(self, data):
        self.task_id = None
        r = requests.post("http://api.captcha.guru/in.php", data=data).text
        print(r)
        if "OK" in r: 
            self.task_id = r.split('|')[1]
            return True
        else: return False
    def getResult(self):
        if self.task_id:
            for i in range(5):
                time.sleep(5)
                url = 'http://api.captcha.guru/res.php?key='+self.api_key+'&id='+self.task_id
                response = requests.get(url).text
                print(response)
                if "OK" in response: return response
        return None
    # def sliderOrSameShapeTikTok(self, type="slider", base64_image=None):
    #     payload = {'body': base64_image, "click":"geetest", "key": self.api_key, "now":"1", "textinstructions": "abc", "type":"base64"}
    #     # payload = {'textinstructions': type, 'click': 'geetest', 'key': self.api_key, 'method': 'base64', 'body': base64_image}
    #     self.createJob(payload)
    #     result = self.getResult()
    #     postion = []
    #     coordinates = result.split(":")[-1]
    #     coordinate = coordinates.split(";")
    #     for i in coordinate:
    #         pos = i.split(",")
    #         for p in pos: postion.append(p.split("=")[-1].strip())
    #     x1, y1, x2, y2 = postion
    #     print(x1, y1, x2, y2)
        
    # def rotatingTikTok(self, base64_image1, base64_image2):
    #     payload = {'textinstructions': 'koleso', 'click': 'geetest', 'key': self.api_key, 'type': 'base64', 'body0': base64_image1, 'body1': base64_image2}
    #     self.createJob(payload)
    #     print(self.getResult())
