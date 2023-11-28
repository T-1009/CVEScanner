import json
import threading

from utils.status import *

from cve.cve20195418 import CVE_2019_5418
from cve.cve20121823 import CVE_2012_1823
from cve.cve20193396 import CVE_2019_3396
from cve.cve201819475 import CVE_2018_19475
from cve.smileFtp import FTPScanner

class cveScanner:
    def __init__(self, host) -> None:
        self.host = host

    def result_append(self, name, flag):
        if flag == 0:
            # print(Yellow + name + ' scanner error !' + Grey)
            message = name + ' scanner error !'
            log_info(message, Yellow)
        elif flag == 1:
            # print(Red + name + ' scanner success !' + Grey)
            message = name + ' scanner success !'
            log_info(message, Red)
        else:
            # print(Green+ name + ' scanner not found !' + Grey)
            message = name + ' scanner not found !'
            log_info(message, Green)

        scan_result.append([name, flag])

    def CVE_2012_1823_scanner(self):
        name = 'CVE-2012-1823'
        cve_2012_1823 = CVE_2012_1823(self.host)
        flag = cve_2012_1823.main()
        self.result_append(name, flag)
    
    def CVE_2018_19475_scanner(self):
        name = 'CVE_2018_19475'
        cve_2018_19475 = CVE_2018_19475(self.host)
        flag = cve_2018_19475.main()
        self.result_append(name, flag)

    def cve_2019_5418_scanner(self):
        name = 'CVE-2019-5418'
        cve_2019_5418 = CVE_2019_5418(self.host)
        flag = cve_2019_5418.main()
        self.result_append(name, flag)

    def cve_2019_3396_scanner(self):
        name = 'CVE-2019-3396'
        cve_2019_3396 = CVE_2019_3396(self.host)
        flag = cve_2019_3396.main()
        self.result_append(name, flag)

    def smile_ftp_scanner(self):
        name = 'Smile vulnerability'
        smile_ftp = FTPScanner(self.host)
        flag = smile_ftp.main()
        self.result_append(name, flag)


    def scan_cve_result_json(self, cve, scan_result, description):
        dict_result = []

        for i in range(len(cve)):
            temp = {}
            temp['漏洞名称'] = cve[i]
            temp['扫描结果'] = scan_result[i][1]
            temp['漏洞描述'] = description[i]
            dict_result.append(temp)

        json_data = json.dumps(dict_result, indent=5, ensure_ascii=False)

        with open('JSON/result.json', 'w', encoding='gbk') as f:
            f.write(json_data)

        message = 'Export scanned files !'
        log_info(message, Green)
        
        # print('\n'+Green + 'Export scanned files !' + Grey)
        
    
    def main(self):
        threads = []

        t1 = threading.Thread(target=self.CVE_2012_1823_scanner())
        t2 = threading.Thread(target=self.CVE_2018_19475_scanner())
        t3 = threading.Thread(target=self.cve_2019_3396_scanner())
        t4 = threading.Thread(target=self.cve_2019_5418_scanner())
        t5 = threading.Thread(target=self.smile_ftp_scanner())

        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        threads.append(t4)
        threads.append(t5)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        
        self.scan_cve_result_json(cve, scan_result, description)