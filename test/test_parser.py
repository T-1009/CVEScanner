import argparse
import sys, os


Green = '\033[92m'
Blue = '\033[94m'
Grey = '\033[0m'
Red = '\033[31m'
White = '\33[97m'
Yellow = '\33[93m'

def banner():
    print(Blue + '''
  _______  __ ____   ______ ____ _____    ____   ____   ___________ 
_/ ___\  \/ // __ \ /  ___// ___\\__  \  /    \ /    \_/ __ \_  __  \_
\  \___\   /\  ___/ \___ \\  \___ / __ \|   |  \   |  \  ___/|  | \/_/
 \___  >\_/  \___  >____  >\___  >____  /___|  /___|  /\___  >__|   
     \/          \/     \/     \/     \/     \/     \/     \/      

    ''' + '\t\tAuthor: T1009\tEmail: 504733997@qq.com' + Grey + '\n\n')

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

def handle_argv():
    args = argv()
    if args.target == None:
        print('no target')
    else:
        print(args.target)

    if args.ping == None:
        print('no ping')
    else:
        print(args.ping)

    if args.port == None:
        print('no port')
    else:
        print(args.port)

if __name__ == '__main__':
    banner()
    args = argv()
    handle_argv()
    print(args)