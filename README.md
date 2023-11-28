# CVEScanner
 Northwestern Polytechnical University Information Security Innovation Experiment Assignment .
 西工大信息安全创新实验大作业
## Usage
![image](https://github.com/T-1009/CVEScanner/assets/102849988/9a9f31d8-e9aa-47c2-a209-f4ee662468ef)

## Function
### Target
**IP: 192.168.203.133**

![image](https://github.com/T-1009/CVEScanner/assets/102849988/ba0a00b2-dad2-4761-ab48-411992693ddc)

### Port Scan
```shell
python3 main.py -pt 192.168.203.133
```

![image](https://github.com/T-1009/CVEScanner/assets/102849988/770a6ca9-939e-4254-91fa-4d36e4a5e288)

### CVE Scan
To use this feature you must use the following format, http or https://url or ip/ such as http://192.168.203.133/ .
```shell
python3 main.py -t http://192.168.203.133/
```

![image](https://github.com/T-1009/CVEScanner/assets/102849988/d7b18cab-2b7d-4b7c-9e31-48feb83c8d87)

### IsAlive Scan
```shell
python3 main.py -t http://192.168.203.133/
python3 main.py -t 192.168.203.133
```

![image](https://github.com/T-1009/CVEScanner/assets/102849988/fbf8dfad-8eec-4559-9d31-4ed7f3f65061)


