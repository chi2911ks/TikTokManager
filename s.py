import requests
from io import BytesIO
import base64
import time

key = '6f4adb5057c229661f831e5b91668cf8'
url1 = b'https://p16-security-va.ibyteimg.com/img/security-captcha-oversea-usa/whirl_e814e0d90e6913de9f1f401f67214565656686e0_1.png~tplv-obj.image'
url2 = b'https://p16-security-va.ibyteimg.com/img/security-captcha-oversea-usa/whirl_e814e0d90e6913de9f1f401f67214565656686e0_2.png~tplv-obj.image'


ee1 = base64.b64encode((url1))
ee2 = base64.b64encode((url2))

payload = {'textinstructions': 'koleso', 'click': 'geetest', 'key': key, 'method': 'base64', 'body0': ee1, 'body1': ee2}
r = requests.post("http://api.captcha.guru/in.php", data=payload)

time.sleep(10)

rt = r.text.split('|')
url = 'http://api.captcha.guru/res.php?key='+key+'&id='+rt[1]

response = requests.get(url)
print(response.content)
