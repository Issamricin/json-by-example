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
class DataEncoder(json.JSONEncoder):
    def default(self, obj):
        if(isinstance(obj, date)):
            return {
                    "__class": "date",
                       "y": obj.year,
                       "month": obj.month,
                       "d":obj.day,
                      }
        elif(isinstance(obj, timedelta)):
            return {
                       "__class": "timedelta",
                       "days":obj.days,
                       "seconds":obj.seconds,
                       "microseconds":obj.microseconds                 
                      }
        elif(isinstance(obj, timezone)):
                return {
                       "__class": "timezone",
                        "offset": obj.utcoffset(None)
                      }

        return super().default(obj)

          
        


class DataDecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=DataDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "date":
            return date(d["y"],d["month"],d["d"])
        elif d.get("__class") == "timedelta":
            return timedelta(d["days"],d["seconds"],d["microseconds"])
        elif d.get("__class") == "timezone":
            return timezone(timedelta(seconds=d["offset"]))  
        return d 
          
                
if __name__=="__main__":
     d=json.loads(data,cls=DataDecoder)
     print(d)
     e=json.dumps(d,cls=DataEncoder, indent=4)
     print(e)
