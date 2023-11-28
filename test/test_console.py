import argparse
import sys, os

from cve.cve20195418 import CVE_2019_5418
from cve.cve20121823 import CVE_2012_1823
from cve.cve20193396 import CVE_2019_3396
from utils.status import *
from utils.ping import *
from utils.status import *
from utils.portScan import portScaner
from utils.cveScan import cveScanner


def banner():
    print(Blue + '''

 ██████╗██╗   ██╗███████╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║     ██║   ██║█████╗  ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║     ╚██╗ ██╔╝██╔══╝  ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╗ ╚████╔╝ ███████╗███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚═════╝  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                      

    ''' + 'Author: T1009\tEmail: 504733997@qq.com' + Grey + '\n\n')

def argv():
    parser = argparse.ArgumentParser(description=Yellow + '[*] Project CVE-Scanner - Manual' + Grey , formatter_class=argparse.ArgumentDefaultsHelpFormatter )
    
    parser.add_argument('-t','--target', help='target to scan',type=str)
    parser.add_argument('-p','--ping', help='check availability of target', type=str)
    parser.add_argument('-pt', '--port', help='Scan target host open ports', type=str)

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        os._exit(0)

    return args


def CVE_2012_1823_scanner(host):
    name = 'CVE-2012-1823'
    cve_2012_1823 = CVE_2012_1823(host)
    flag = cve_2012_1823.main()
    result_append(name, flag)

def cve_2019_5418_scanner(host):
    name = 'CVE-2019-5418'
    cve_2019_5418 = CVE_2019_5418(host)
    flag = cve_2019_5418.main()
    result_append(name, flag)

def cve_2019_3396_scanner(host):
    name = 'CVE-2019-3396'
    cve_2019_3396 = CVE_2019_3396(host)
    flag = cve_2019_3396.main()
    result_append(name, flag)
    
def cve_scanner(host):
    print(Yellow + '                ***  CVE Scanner Start  ***             ' + Grey + '\n')
    CVE_2012_1823_scanner(host)
    cve_2019_5418_scanner(host)
    cve_2019_3396_scanner(host)
    print('\n'+ Yellow + '                ***  CVE Scanner End  ***               ' + Grey + '\n\n')

def ping_isAlive(host):
    try:
        flag = is_alive(host)
        if flag == True:
            print(Green + host + ' is online !\n' + Grey)
        else:
            print(Red + host + ' is offline !\n' + Grey)
    except:
        pass

def port_scanner(host):
    print(Yellow + '                ***  Port Scanner Start  ***                ' + Grey + '\n')
    try:
        flag = is_alive(host)
        if flag == True:
            print(Green + host + ' is online !\n' + Grey)
            port_scan = portScaner(host)
            port_scan.main()
            print()
        else:
            print(Red + host + ' is offline !\n' + Grey)
    except:
        pass
    print('\n'+ Yellow + '                ***  Port Scanner End  ***              ' + Grey + '\n\n')

def result_append(name, flag):
    if flag == 0:
        print(Yellow + name + ' scanner error !' + Grey)
    elif flag == 1:
        print(Red + name + ' scanner success !' + Grey)
    else:
        print(Green+ name + ' scanner not found !' + Grey)

    scan_result.append([name, flag])

def scan_cve_result_json(cve, scan_result, description):
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

def write_info():
    print(Yellow + '                ***  Report Export Start  ***               ' + Grey + '\n')
    scan_cve_result_json(cve, scan_result, description)
    print(Green + 'Export scanned files !' + Grey)
    print('\n'+ Yellow + '                ***  Report Export End  ***             ' + Grey + '\n\n')

def run():
        
    os.system('cls')
    banner()

    args = argv()

    if args.target == None:
        pass
    else:
        HOST = args.target
        cve_scanner(HOST)
        write_info()

    if args.ping == None:
        pass
    else:
        HOST = args.ping
        ping_isAlive(HOST)

    if args.port == None:
        pass
    else:
        HOST = args.port
        port_scanner(HOST)

