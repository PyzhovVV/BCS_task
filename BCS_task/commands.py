import requests
import json


class Methods:
    def __int__(self):
        self.url = "http://bcs_tester:iLoveBCS@45.32.232.25:3669/wallet/"

    def sendrwquest(self, command, data):
        data = {"method": command}
        if data:
            data["params"] = data
        res_json = requests.post(self.url, data=json.dumps(data)).json()
        if res_json['error']:
            print(res_json['error'])
            return None
        return res_json['result']

    def getnewaddress(self):
        payload = {
            "method": "getnewaddress",
        }
        response = requests.post(
            self.url, data=json.dumps(payload)).json()
        return response['result']

