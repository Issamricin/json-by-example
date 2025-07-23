import json
from email.message import EmailMessage
from ipaddress import IPv4Address
from urllib.parse import ParseResult

data = """{
    "sender": {
        "__class": "EmailMessage",
        "headers": {
            "From": "admin@example.com",
            "To": "user@client.com",
            "Subject": "Access Granted"
        },
        "body": "Welcome! Your access has been granted. Click the link below."
    },
    "client_ip": {
        "__class": "IPv4Address",
        "address": "192.168.1.42"
    },
    "link": {
        "__class": "ParseResult",
        "scheme": "https",
        "netloc": "portal.example.com",
        "path": "/welcome",
        "params": "",
        "query": "token=abc123",
        "fragment": ""
    }
}"""
class linkdecoder(json.JSONDecoder):
    def _init__(self):
        json.JSONDecoder.__init__(self, object_hook=linkdecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "ParsResult":
            return ParseResult(d["scheme"],d["netloc"],["path"],["params"],["query"],d["fragment"])

        return 
if __name__=="__main__":
    d=json.loads(data)
    sender=d["sender"]
    print(sender)
    l=json.loads(data,cls=linkdecoder)
    print(type(l))