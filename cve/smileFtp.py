from socket import *
from ftplib import FTP
from urllib.parse import urlparse

from utils.status import *
from utils.console import *

class FTPScanner:
    def __init__(self, host) -> None:
        self.host = urlparse(host).hostname
        self.port = 21
        self.rport = 6200

    def main(self):
        s = socket(AF_INET, SOCK_STREAM) #使用socket函数来检测是否有漏洞存在
        res = s.connect_ex((self.host, self.rport))
        if res != 0:
            message = 'Before verification Smile vulnerability Port 6200 is not open !'
            log_info(message, Blue)
            # print(Green + "Before verification Smile vulnerability Port 6200 is not open !" + Grey)

        ftp = FTP()
        username = 'root:)' # 用户名必须包含：)这两个字符
        password = 'anonymous' # 密码随便啥都行
        try:
            ftp.connect(self.host, self.port, timeout=10)#使用ftp登录，设置延时10秒
            ftp.login(username,password)
            ftp.quit()
        except:
            message = "Complete login check !"
            log_info(message, Green)
            # print(Green + "Complete login check !" + Grey)

        try:
            s = socket(AF_INET, SOCK_STREAM) # 使用socket函数来检测是否有漏洞存在
            res = s.connect_ex((self.host, self.rport))
            if res == 0:
                return SUCCESS
                
            else:
                s.close()
                message = "Port 6200 is not open !"
                log_info(message, Green)
                # print(Green + "Port 6200 is not open !" + Grey)
                return FAILED   
            
        except:
            return ERROR




 