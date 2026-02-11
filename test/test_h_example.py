import json
import pytest
from email.message import EmailMessage
from ipaddress import IPv4Address
from urllib.parse import ParseResult
from src.json_by_example.h_example import decodTypes, EncodeTypes


@pytest.fixture
def test_data():
    return """{
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


def test_decodeDataTypes(test_data):
    decode = json.loads(test_data, object_hook=decodTypes)
    assert isinstance(decode["client_ip"], IPv4Address)
    assert isinstance(decode["link"], ParseResult)
    assert isinstance(decode["sender"], EmailMessage)


def test_encodeDataTypes(test_data):
    decode = json.loads(test_data, object_hook=decodTypes)
    encode = json.dumps(decode, cls=EncodeTypes)
    assert json.loads(encode) == json.loads(test_data)
