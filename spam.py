#!/usr/bin/python
# Author: https://vk.com/id181265169

import vk, urllib.request, urllib.error, urllib.parse, json, random, time

username = input("Login:")
password = input("Password:")

url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (username, password)

try:
    r = urllib.request.urlopen(url)
except urllib.error.HTTPError:
    print("�� ���������� �������������� (�������� ����������� ������� ����� ��� ������)")
    quit(1)

r = r.read()
token = json.loads(r)["access_token"] 
session = vk.Session(access_token = token)
vk = vk.API(session)

foo = ["hi", "2", "3", "fuck", "5"]

# print (foo)

victim = input("User id: ")

r = vk.users.get(user_id = victim, fields = "id", v = 5.73)
r = r[0]["id"]

victim = r

while(True):
	try:
		time.sleep(random.randint(1,3) + random.randint(1,4))
		r = vk.messages.send(peer_id = victim, message = random.choice(foo), v = 5.73)
		print()
		print("wait...")
		time.sleep(random.randint(1,2) + random.randint(1,2))
		print("done  ",random.choice(foo))
	except:
		pass
