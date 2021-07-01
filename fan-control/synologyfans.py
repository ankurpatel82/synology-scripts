import sys
import http.client
import json

api_username = 'apiuser'
api_password = 'apipassword'
server_url = 'serverurl'
fan_setting = sys.argv[1]
server_connection = http.client.HTTPSConnection(server_url, 5001)

print("Starting Authentication Process")
server_connection.request("GET", "/webapi/auth.cgi?api=SYNO.API.Auth&version=3&method=login&account=" + api_username + "&passwd=" + api_password + "&format=cookie&enable_syno_token=yes", '', {})
auth_response = server_connection.getresponse()
auth_json = json.loads(auth_response.read().decode('utf-8'))
print("Authentication Success: " + str(auth_json["success"]))

print("Starting Fan Update Process - Fan Setting: " + fan_setting)
payload = 'compound=%5B%7B%22api%22%3A%22SYNO.Core.Hardware.FanSpeed%22%2C%22method%22%3A%22set%22%2C%22version%22%3A%221%22%2C%22dual_fan_speed%22%3A%22' + fan_setting + '%22%7D%5D&api=SYNO.Entry.Request&method=request&version=1'
headers = {
  'x-syno-token': auth_json["data"]["synotoken"], 
  'Cookie': 'did=' + auth_json["data"]["did"] +'; id=' + auth_json["data"]["sid"]
}
server_connection.request("POST", "/webapi/entry.cgi", payload, headers)
fan_response = server_connection.getresponse()
fan_json = json.loads(fan_response.read().decode('utf-8'))
print("Fan Update Success: " + str(fan_json["success"]))
