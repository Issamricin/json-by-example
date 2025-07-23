import json
from datetime import date,timedelta,timezone

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


class DateTimeEncoder(json.JSONEncoder):
     
     def default(self, obj):
            if(isinstance(obj, date)):
                return {
                       "__class": "date",
                       "y": obj.year,
                       "month": obj.month,
                       "d":obj.day,
                       
                      }
          
            return json.JSONEncoder.default(self,obj) 

class DatetimeDecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=DatetimeDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "date":
            return date(d["y"],d["month"],d["d"])
                
        return d 
          

class TimeDeltaEncoder(json.JSONEncoder):
     
     def default(self, obj):
            if(isinstance(obj, timedelta)):
                return {
                       "__class": "timedelta",
                       "days":obj.days,
                       "seconds":obj.seconds,
                       "microseconds":obj.microseconds                 
                      }
          
            return json.JSONEncoder.default(self,obj) 
     
class TimeDeltaDecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=TimeDeltaDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "timedelta":
            return timedelta(d["days"],d["seconds"],d["microseconds"])
                
        return d 
          

class TimeZoneEncoder(json.JSONEncoder):
     
     def default(self, obj):
            if(isinstance(obj, timezone)):
                return {
                       "__class": "timezone",
                       "offset":obj.utcoffset
                      }
          
            return json.JSONEncoder.default(self,obj) 
          
        
class TimeZoneDecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=TimeZoneDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "timezone":
            return timezone(timedelta(seconds=d["offset"]))
                
        return d 
    
          
if __name__=="__main__":
     date_d=json.loads(data,cls=DatetimeDecoder)
     print(date_d)
     date_e=json.dumps(date_d,cls=DateTimeEncoder)

     delta_d=json.loads(data,cls=TimeDeltaDecoder)
     print(delta_d)
     delta_e=json.dumps(delta_d,cls=TimeDeltaEncoder)

     zone_d=json.loads(data,cls=TimeZoneDecoder)
     print(zone_d)
