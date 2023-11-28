from socket import *
import time
import threading

SERVER = {
    'FTP': '21',
    'SSH': '22',
    'Telnet': '23',
    'SMTP': '25',
    'DNS': '53',
    'DHCP': '68',
    'HTTP': '80',
    'TFTP': '69',
    'WWW': '8080',
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
    'Hadoop': '50070',
    'smile': '6200'
}

def get_server(port):
    global SERVER
    for k, v in SERVER.items():
        if v == port:
            return k
    return 'Unknown'

def socket_scan(host, port, server):
    tcp = socket(AF_INET, SOCK_STREAM)
    try:
        tcp.settimeout(3)
        result = tcp.connect_ex((host, int(port)))
        if result == 0:
            server.append([get_server(port), port])
        else:
            pass
    except Exception as e:
        pass
    finally:
        try:
            tcp.close()
        except:
            pass

def main():
    host = '192.168.203.133'
    port_list = [v for _, v in SERVER.items()]
    print(port_list)

    server = [] # [[server, port], ...,]

    threads = []
    for port in port_list:
        t = threading.Thread(target=socket_scan, args=(host, port, server))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    
    server = sorted(server, key=lambda x: int(x[1]))

    print('{:<20}\t\t{:<20}\t\t{:<20}'.format('Server', 'Port', 'State'))
    for i in server:
        print('{:<20}\t\t{:<20}\t\t{:<20}'.format(i[0], i[1], 'open'))

if __name__ == '__main__':
    s = time.time()
    main()
    e = time.time()
    print('Spend time: {} s'.format(e-s))