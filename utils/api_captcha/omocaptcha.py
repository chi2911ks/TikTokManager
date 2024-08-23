


from time import sleep

import requests


class Omocaptcha:
    def __init__(self, key) -> None:
        self.key = key
        self.headers = {"Content-Type": "application/json"}
        self.id = None
    def checkValidKey(self):
        try:
            return not requests.post('https://omocaptcha.com/api/getBalance', json={"api_token": self.key}, headers=self.headers).json()["error"]
        except: return False
    def getBalance(self):
        return float(requests.post('https://omocaptcha.com/api/getBalance', json={"api_token": self.key}, headers={"Content-Type": "application/json"}).json()["balance"])
    def createJob(self, **kwargs):
        
        data = {
            "api_token": self.key,
        }
        data.update(kwargs)
        createjob = requests.post('https://omocaptcha.com/api/createJob', json=data, headers=self.headers).json()
        print(createjob)
        if createjob["success"]: self.id = createjob["job_id"]
    def getJobResult(self, time_solve:int=15):
        if self.id is None:
            return None
        data = {"api_token": self.key, "job_id": self.id}
        for i in range(time_solve*4):
            try:
                result = requests.post("https://omocaptcha.com/api/getJobResult", json=data, headers=self.headers).json()
                if result["status"] == "success":
                    return result["result"]
                elif result["status"] == "fail":
                    return None
            except: return None
            sleep(0.25)