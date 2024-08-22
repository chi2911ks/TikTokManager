from time import sleep
import requests

class Proxy:
    def __init__(self, domain, api_key):
        self.domain = domain
        self.api_key = api_key
        self.host = None
        self.port = None
        self.__getHost()
        self.__getPort()
    def checkProxy(self, ip):
        try:
            proxies = {
                "http": "http://"+ip,
                "https": "http://"+ip,
            }
            return requests.get('https://api64.ipify.org/?format=json', proxies=proxies, timeout=20).json()["ip"]
            return True
        except: return False
    def changeIP(self, new=False):
        while True:
            try:
                change = requests.get("http://%s/vi/api/wanv1?key=%s&act=changipproxy"%(self.domain, self.api_key)).json()
                print(change)
                if change["result"] == "success":
                    while True:
                        sleep(5)
                        try:
                            ip = requests.get("http://%s/vi/api/wanv1?key=%s&act=getip"%(self.domain, self.api_key)).json()
                            print(ip)
                            if ip["data"]["ipv4_wan"] is not None:
                                return ip["data"]["ipv4_wan"]
                        except: pass
                if not new: break
                elif change["result"] == "unsuccess": sleep(60)
            except: pass
    def __getPort(self):

        self.port = requests.get("http://%s/vi/api/wanv1?key=%s&act=getip"%(self.domain, self.api_key)).json()["data"]["port_listen_ipv4"]
        
    def __getHost(self):
        self.host =  self.domain.split(":")[0]
    def getIP(self):
        return "%s:%s"%(self.host, self.port)
# p = Proxy("maidinhduongpro.ddnsfree.com:8080", "048mxXL9FgRMk4dIVmTUSYlhF3A36KD8")
# # p.changeIP()
# # print(p.getIP())
# print(p.checkProxy("maidinhduongpro.ddnsfree.com:1854"))
