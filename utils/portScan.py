from socket import *
import threading

from utils.status import *


class portScaner:
    def __init__(self, host) -> None:
        global SERVER
        self.port = [v for _, v in SERVER.items()]
        self.host = host

    def get_server(self, port):
        global SERVER
        for k, v in SERVER.items():
            if v == port:
                return k
        return 'Unknown'

    def socket_scan(self, host, port, server):
        tcp = socket(AF_INET, SOCK_STREAM)
        try:
            tcp.settimeout(5)
            result = tcp.connect_ex((host, int(port)))
            if result == 0:
                server.append([self.get_server(port), port])
        except Exception as e:
            pass
        finally:
            try:
                tcp.close()
            except:
                pass

    def main(self):
        host = self.host
        port_list = [v for _, v in SERVER.items()]

        server = [] # [[server, port], ...,]

        threads = []
        for port in port_list:
            t = threading.Thread(target=self.socket_scan, args=(host, port, server))
            threads.append(t)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        
        server = sorted(server, key=lambda x: int(x[1]))

        print('{}{:<20}\t\t{:<20}\t\t{:<20}{}'.format(Yellow, 'SERVER', 'PORT', 'STATE', Grey))
        for i in server:
            print('{}{:<20}\t\t{:<20}\t\t{}{:<20}{}'.format(White, i[0], i[1], Green, 'open', Grey))
