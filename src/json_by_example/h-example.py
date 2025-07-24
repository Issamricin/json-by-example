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
          
class DataDecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=DataDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "IPv4Address":
            return IPv4Address(d["address"])
        elif d.get("__class") == "ParseResult":
            return ParseResult(d["scheme"],d["netloc"],d["path"],d["params"],d["query"],d["fragment"])
        elif d.get("__class") == "EmailMessage":
             msg=EmailMessage()
             msg["From"]=d["headers"]["From"]
             msg["To"]=d["headers"]["To"]
             msg["Subject"]=d["headers"]["Subject"]
             msg.set_content(d["body"])
             return msg
        
        return d 
class DataEncoder(json.JSONEncoder):
     
     def default(self, obj):
            if(isinstance(obj, IPv4Address)):
                return {
                       "__class": "IPv4Address",
                       "address":obj.compressed
                      }
            elif(isinstance(obj, ParseResult)):
                return {
                       "__class": "ParseResult",
                        "scheme":obj.scheme,
                        "netloc":obj.netloc,
                        "path":obj.path,
                        "params":obj.params,
                        "query":obj.query,
                        "fragment":obj.fragment
  
                      }
            elif(isinstance(obj, EmailMessage)):
                 return{
                      "__class":"EmailMessage",
                      "headers":{
                           "From":obj["From"],
                           "To":obj["To"],
                           "Subject":obj["Subject"]
                      },
                      "body":obj.get_content()

                 }

       
            return json.JSONEncoder.default(self,obj) 
     
if __name__=="__main__":
    d=json.loads(data,cls=DataDecoder)
    d_email=d["sender"]
    print(d_email)
    d_ip=str(d["client_ip"])
    print(d_ip)
    d_link=d["link"].geturl()
    print(d_link)
    e=json.dumps(d,cls=DataEncoder,indent=4)
    print(e)
