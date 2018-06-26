import urllib.request
import json
ioinfo = urllib.request.urlopen('https://ipinfo.io/geo?token=dc51d5e7c40c75')
ioinfo = ioinfo.read()
data = json.loads(ioinfo)
print(data)