

import socket
import ssl
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

port = 0

url = input("Type in URL: ")
f_url = url.strip()

try:
    print("Using Regex and Sockets")
    try:
        host_url = re.search("http[s]*\://(.*?)[/]|http[s]*\://(.*)", url, re.IGNORECASE).group(1)

        secure = re.findall("http([s]):", url)

        print("Host URL: ", host_url)

        if len(secure) > 0:
            port = 443
        else:
            port = 80

        print("Port: ", port)


        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host_url, port))
        cmd = 'GET f_url HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1: break
            print(data.decode(),end='')

        mysock.close()
    except:
        exit()    


except:
    print("Using BeautifulSoup")
    html = urllib.request.urlopen(f_url, context=ctx).read() # opens webpage in read mode
    soup = BeautifulSoup(html, 'html.parser') # html is passed to the soup html parser and saved as soup

    print(soup)
# Retrieve all of the anchor tags
#for tag in tags: # from each tag it gets the href attribute and prints it
#    print(tag.get('href', None))
