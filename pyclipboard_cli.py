import sys
import requests
from requests.auth import HTTPBasicAuth

Backend = 'http://localhost:10000/clipboard'

if len(sys.argv) == 5:
	Program, User, Pwd, Content, Expiry = sys.argv
	Expiry = int(Expiry)
	payload = {
		'User':User,
		'Pwd':Pwd,
		'Content':Content,
		'Expiry':Expiry
	}
elif len(sys.argv) == 3:
	Program, User, Pwd = sys.argv
else:
	print("This is not a valid option!")

if len(sys.argv) == 5:
	Result = requests.post(url=Backend, data = payload)
else:
	Result = requests.get(url=Backend, auth = HTTPBasicAuth(User,Pwd))


print(f"Status Code: {Result.status_code}, Message: {Result.text}")
