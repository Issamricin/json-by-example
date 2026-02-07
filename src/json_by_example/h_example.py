import json
from email.message import EmailMessage
from ipaddress import IPv4Address
from urllib.parse import ParseResult


class EncodeTypes(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, EmailMessage):
            return {
                "__class": "EmailMessage",
                "headers": dict(o.items()),
                "body": o.get_content(),
            }
        if isinstance(o, IPv4Address):
            # print(o)
            return {"__class": "IPv4Address", "address": str(o)}
        if isinstance(o, ParseResult):
            # print(
            #     f"__class: ParseResult,scheme: {o.scheme},netloc:{o.netloc},path: {o.path},params: {o.params},query :{o.query},fragment : {o.fragment}"
            # )
            return {
                "__class": "ParseResult",
                "scheme": o.scheme,
                "netloc": o.netloc,
                "path": o.path,
                "params": o.params,
                "query": o.query,
                "fragment": o.fragment,
            }
        return super().default(o)


def decodTypes(dic):
    if dic.get("__class") == "EmailMessage":
        return {
            "__class": "EmailMessage",
            "headers": dic["headers"],
            "body": dic["body"],
        }
    if dic.get("__class") == "IPv4Address":
        return IPv4Address(dic["address"])
    if dic.get("__class") == "ParseResult":
        return {
            "__class": "ParseResult",
            "scheme": dic["scheme"],
            "netloc": dic["netloc"],
            "path": dic["path"],
            "params": dic["params"],
            "query": dic["query"],
            "fragment": dic["fragment"],
        }
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
