import argparse
import sys, os

from utils.status import *
from utils.ping import *
from utils.portScan import portScaner
from utils.cveScan import cveScanner


def banner():
    print(Magenta + '''
   ______          _____                                 
  / ____/   _____ / ___/_________ _____  ____  ___  _____
 / /   | | / / _ \\\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
/ /___ | |/ /  __/__/ / /__/ /_/ / / / / / / /  __/ /    
\____/ |___/\___/____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                         

    ''' + '\tAuthor: T1009\tEmail: 504733997@qq.com' + Grey + '\n\n')


def argv():
    parser = argparse.ArgumentParser(description=Yellow + '[*] Project CVE-Scanner - Manual' + Grey,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-t', '--target', help='target to scan', type=str)
    parser.add_argument('-p', '--ping', help='check availability of target', type=str)
    parser.add_argument('-pt', '--port', help='Scan target host open ports', type=str)

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        os._exit(0)

    return args


def cve_scanner(host):
    print(Yellow + '                ***  CVE Scanner Start  ***             ' + Grey + '\n')
    cve_scanner = cveScanner(host)
    cve_scanner.main()
    print('\n' + Yellow + '                ***  CVE Scanner End  ***               ' + Grey + '\n\n')


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
    print('\n' + Yellow + '                ***  Port Scanner End  ***              ' + Grey + '\n\n')


def run():
    os.system('cls')
    banner()
    args = argv()

    if args.target == None:
        pass
    else:
        HOST = args.target
        cve_scanner(HOST)

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
