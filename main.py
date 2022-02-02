import json
import requests
r"""
photonum = input("enter number of picture: ")
photourl = " http://jsonplaceholder.typicode.com/photos/" + photonum
mydict = requests.get(photourl)

while mydict.status_code >= 400 < 500:
    print("there was some kind of error, try another num")
    photonum = input("enter number of picture: ")
    photourl = " http://jsonplaceholder.typicode.com/photos/" + photonum
    mydict = requests.get(photourl)

mydict = mydict.content
mydict = json.loads(mydict)

print(type(mydict))

class photostock:
    def __init__(self, d):
        self.__dict__ = d
    def __str__(self):
        print("the following keys are in the instance")
        for k in self.__dict__:
            print(k)

photo1 = photostock(mydict)
photo1.__str__()
"""

url = "http://jsonplaceholder.typicode.com/users"

userlist = requests.get(url)
userlist = userlist.content
userlist = json.loads(userlist)

uname = input("enter your name: ")
savedict = None

for name in userlist:
    if str(name["name"]).lower() == uname.lower():
        print(f"there is a match for your name {name['name']}")
        savedict = name
    if uname.lower() in str(name["name"]).lower() and uname.lower() != str(name["name"]).lower():
        print(f"there is a partial match in the following name ==> {name['name']}")


class Users:
    def __init__(self, d):
        self.__dict__ = d


class Adresses:
    def __init__(self, d):
        self.__dict__ = d


if savedict is not None:
    geo = savedict["address"]
    del savedict["address"]
    user1 = Users(savedict)
    print(user1.__dict__)
    address1 = Adresses(geo)
    print(address1.__dict__)
