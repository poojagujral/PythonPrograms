from urllib.parse import urlparse

html = urlparse('https://www.google.co.uk/search?q=hey+google&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjJl-7r_u7bAhWLOo8KHQkcAv0Q_AUIDSgE&biw=1366&bih=700')
#print(html)


x = 'https://console.aws.amazon.com/console/home?param1=val1&param2=val2'


def url_parse(x):
    a=x.split('?')[1]
    b=a.split('&')
    d={}
    print(a)
    print(b)
    for i in b:
        d[i.split('=')[0]] = i.split('=')[1]
    print(d)

url_parse(x)