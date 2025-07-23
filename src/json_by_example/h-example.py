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

class EmailEncoder(json.JSONEncoder):
     
     def default(self, obj):
            if(isinstance(obj, EmailMessage)):
                return {
                       "__class": "EmailMessage",
                       
                      }
          
            return json.JSONEncoder.default(self,obj) 
     
        
class EmailDecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=EmailDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "EmailMessage":
            return EmailMessage(d["y"],d["month"],d["d"],d["h"],d["minute"],d["s"])
                
        return d 
          
class IPEncoder(json.JSONEncoder):
     
     def default(self, obj):
            if(isinstance(obj, IPv4Address)):
                return {
                       "__class": "IPv4Address",
                       "address":obj.compressed
                      }
          
            return json.JSONEncoder.default(self,obj)  
          
class IPDecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=IPDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "IPv4Address":
            return IPv4Address(d["address"])
                
        return d 
        
     

class LinkEncoder(json.JSONEncoder):
     
     def default(self, obj):
            if(isinstance(obj, ParseResult)):
                return {
                       "__class": "ParseResult",
                        "scheme":obj.scheme,
                        "netloc":obj.netloc,
                        "path":obj.path,
                        "params":obj.params,
                        "query":obj.query,
                        "fragment":obj.fragment
  
                      }
          
            return json.JSONEncoder.default(self,obj) 
          
class LinkDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=LinkDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "ParseResult":
            return ParseResult(d["scheme"],d["netloc"],d["path"],d["params"],d["query"],d["fragment"])
                
        return d 
    

if __name__=="__main__":
     d_link=json.loads(data,cls=LinkDecoder) 
     #print(d_link["link"].geturl())
     e_link=json.dumps(d_link,cls=LinkEncoder)
     #print(e_link)
     d_ip=json.loads(data,cls=IPDecoder)
     ip=str(d_ip["client_ip"])
     print(ip)
     e_ip=json.dumps(d_ip,cls=IPEncoder)
     #print(e_ip)
