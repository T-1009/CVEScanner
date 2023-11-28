from socket import *

def socket_scan(host, port):
    tcp = socket(AF_INET, SOCK_STREAM)
    try:
        tcp.settimeout(3)
        result = tcp.connect_ex((host, int(port)))
        if result == 0:
            print('success !')
        else:
            pass
    except Exception as e:
        pass
    finally:
        try:
            tcp.close()
        except:
            pass

socket_scan('192.168.203.133', 6200)