import json, random
import platform
import subprocess
import requests

def ping_ip(ip):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', ip]
    if subprocess.call(command, stdout=subprocess.DEVNULL) == 0:
        return True
    return False

def request_url(url):
    # headers = {
    #             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
    #         }
    with open('JSON/agent.json', 'r') as f:
            a = json.load(f)['header']
            headers = str(random.choice(a)).strip("{").strip("}")
    try:
        response = requests.get(url, headers, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False


def is_alive(host):
    if ping_ip(host):
        return True
    if request_url(host):
        return True
    return False