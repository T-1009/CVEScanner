Green = '\033[92m'
Blue = '\033[94m'
Grey = '\033[0m'
Red = '\033[31m'
White = '\33[97m'
Yellow = '\33[93m'
Magenta = '\33[95m'
Pink = '\033[38;5;218m'

ERROR   = 0
SUCCESS = 1
FAILED  = 2
WARNING = 3
UNKNOWN = 4
INFO    = 5
LOG     = 6

cve = ['CVE-2012-1823', 'CVE-2018-19475',  'CVE-2019-3396', 'CVE-2019-5418','Smile vulnerability']

scan_result = []

description = ['关于PHP代码注入漏洞的公开漏洞，该漏洞允许攻击者通过构造恶意输入来执行任意的PHP代码, 攻击者可以利用它来执行任意系统命令、获取敏感信息、篡改数据等。',
               '关于LibTIFF在处理特定的TIFF图像文件时存在的堆缓冲区溢出漏洞，漏洞可能允许远程攻击者执行任意代码或导致拒绝服务（DoS）攻击',
               '关于Confluence服务器的公开漏洞， 该漏洞允许攻击者在未经授权的情况下读取和下载Confluence服务器上的任意文件，包括配置文件、数据库凭证和其他敏感信息。',
               '关于Rails文件泄露漏洞的公开漏洞， 该漏洞源于Rails的Action Pack组件对于某些文件路径处理不当，攻击者可以通过构造恶意请求访问服务器上的任意文件，并将其下载到本地。',
               'FTP版本2.3.4，发送的用户名后面加上":)"，密码任意，这个版本的后门会在6200端口上打开一个监听的shell，攻击者可以通过telnet确认或者通过metasploit上面的攻击模块自动攻击'
               ]

HOST = ''

SERVER = {
    'FTP': '21',
    'SSH': '22',
    'Telnet': '23',
    'SMTP': '25',
    'DNS': '53',
    'DHCP': '68',
    'HTTP': '80',
    'TFTP': '69',
    'HTTP-WWW': '8080',
    'POP3': '995',
    'NetBIOS': '139',
    'IMAP': '143',
    'HTTPS': '443',
    'SNMP': '161',
    'LDAP': '489',
    'SMB': '445',
    'SMTPS': '465',
    'Linux R RPE': '512',
    'Linux R RLT': '513',
    'Linux R cmd': '514',
    'Rsync': '873',
    'IMAPS': '993',
    'Proxy': '1080',
    'JavaRMI': '1099',
    'Lotus': '1352',
    'MSSQL': '1433',
    'MSSQL': '1434',
    'Oracle': '1521',
    'PPTP': '1723',
    'cPanel': '2082',
    'CPanel': '2083',
    'Zookeeper': '2181',
    'Docker': '2375',
    'Zebra': '2604',
    'MySQL': '3306',
    'Kangle': '3312',
    'RDP': '3389',
    'SVN': '3690',
    'Rundeck': '4440',
    'GlassFish': '4848',
    'PostgreSql': '5432',
    'PcAnywhere': '5632',
    'VNC': '5900',
    'CouchDB': '5984',
    'varnish': '6082',
    'Redis': '6379',
    'Weblogic': '7001',
    'Kloxo': '7778',
    'Zabbix': '8069',
    'RouterOS': '8291',
    'Elasticsearch': '9200',
    'Elasticsearch': '9300',
    'Zabbix': '10050',
    'Zabbix': '10051',
    'Memcached': '11211',
    'MongoDB': '27017',
    'MongoDB': '28017',
    'Hadoop': '50070'
}

import datetime

def log_info(message, color):
    current_time = datetime.datetime.now().strftime("[%H:%M:%S]")
    print("{}{} {}INFO -- {}{}".format(Yellow, current_time, color, message, Grey))