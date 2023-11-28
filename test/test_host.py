from urllib.parse import urlparse

url = "https://192.168.203.133/"
parsed_url = urlparse(url)
hostname = parsed_url.hostname

print(hostname)
