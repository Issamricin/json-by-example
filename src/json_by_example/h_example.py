import json
from email.message import EmailMessage
from ipaddress import IPv4Address
from urllib.parse import ParseResult


class EncodeTypes(json.JSONEncoder):
    def encode(self, o):
        if isinstance(o, dict):
            return super().encode({k: self.transform_special(v) for k, v in o.items()})

    def transform_special(self, o):
        if isinstance(o, ParseResult):
            return {
                "__class": "ParseResult",
                "scheme": o.scheme,
                "netloc": o.netloc,
                "path": o.path,
                "params": o.params,
                "query": o.query,
                "fragment": o.fragment,
            }
        return o

    def default(self, o):
        if isinstance(o, EmailMessage):
            return {
                "__class": "EmailMessage",
                "headers": {
                    k: v for k, v in o.items() if k in ("From", "To", "Subject")
                },
                "body": o.get_content().rstrip("\n"),
            }
        if isinstance(o, IPv4Address):
            # print(o)
            return {"__class": "IPv4Address", "address": str(o)}
        return super().default(o)


def decodTypes(dic):
    if "__class" not in dic:
        return dic
    if dic.get("__class") == "EmailMessage":
        msg = EmailMessage()
        for key, value in dic["headers"].items():
            msg[key] = value
        msg.set_content(dic["body"])
        return msg
    if dic.get("__class") == "IPv4Address":
        return IPv4Address(dic["address"])
    if dic.get("__class") == "ParseResult":

        return ParseResult(
            dic["scheme"],
            dic["netloc"],
            dic["path"],
            dic["params"],
            dic["query"],
            dic["fragment"],
        )
    return dic


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
decode = json.loads(data, object_hook=decodTypes)
print("Decoded : ")
print(decode)
encode = json.dumps(decode, cls=EncodeTypes, indent=4)
print("Encoded : ")
print(encode)
