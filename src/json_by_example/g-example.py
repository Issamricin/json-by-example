import json
from datetime import date,timedelta,timezone,datetime

data = """{
    "report": {
        "created": {
            "__class": "date",
            "y": 2025,
            "month": 4,
            "d": 27
        },
        "duration": {
            "__class": "timedelta",
            "days": 2,
            "seconds": 3600,
            "microseconds": 4
        },
        "timezone": {
            "__class": "timezone",
            "offset": 2
        }
    }
}"""

class datetimeencoder(json.JSONEncoder):
    def default(self, obj):
        if (isinstance(obj,datetime)):
            return{
                "__class":"date",
                "y":obj.year,
                "month":obj.month,
                "d":obj.day
            }
        return json.JSONEncoder.default(self,obj)
        
class datatimedecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=datatimedecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "date":
            return datetime(d["y"],d["month"],d["d"])

        return d 


    

class timedeltaencoder(json.JSONEncoder):
    def default(self, obj):
        if (isinstance(obj,timedelta)):
            return{
                "__class":"timedelta",
                "H":obj.hour,
                "M":obj.minute,
                "S":obj.second
            }
        return json.JSONEncoder.default(self,obj)
    

class timedeltadecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=timedeltadecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class")=="timedelta":
            return timedelta(d["days"],d["seconds"],d["microseconds"])
        return d 
    
class timezoneencoder(json.JSONEncoder):
    def default(self, obj):
        if (isinstance(obj,timezone)):
            return{
                "__class":"timezone",
                "offset":obj.utcoffset
            }
        return json.JSONEncoder.default(self,obj)
    

class timezonedecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=timezonedecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class")=="timezone":
            return timezone(d["offset"])
        return d 

if __name__ =='__main__':
    d=json.loads(data)
    print(type(d))
    x1=json.dumps(d["report"]["created"],cls=datetimeencoder)
    print(x1)
    print(type(x1))
    x2=json.dumps(d["report"]["duration"],cls=timedeltaencoder)
    print(x2)
    x3=json.dumps(d["report"]["timezone"],cls=timezoneencoder)
    print(x3)
    timedeltadec=json.loads(data,cls=timedeltadecoder)
    print(timedeltadec)
    print(type(timedeltadec))

    #x4=json.dumps(data,cls=datetimeencoder,cls=timedeltaencoder,cls=timezoneencoder) wrong
