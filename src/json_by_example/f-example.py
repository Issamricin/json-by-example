'''
In case we have encoded the complex number into JSON Object as list, it will not be possible
 to decoded or convert to pyth complex datatype
 In this example we want to encode and decode complex and datetime
JSON Object below:

 {
    "signal": {
        "place": "Uppsala",
        "stamp": {
            "__class": "datetime",
            "y": 2025,
            "month": 4,
            "d": 19,
            "h": 16,
            "minute": 23,
            "s": 51
        },
        "samples:": [
            {
                "__class": "complex",
                "real": -2.0,
                "imag": 5.0
            },
            {
                "__class": "complex",
                "real": 3.0,
                "imag": 1.0
            },
            {
                "__class": "complex",
                "real": 2.0,
                "imag": 5.0
            }
        ]
    }
}
 

You can see the samples is a list of complex numbers and we have stamps
Use the examples in the previous files (module)  to Decode and Encode the above JSON file
You can see the Python object structure below.
Try to debug your result so you can inspect and see how dictionary is format from the JSON object String 
'''
import json
from datetime import datetime
class Signal():
    def __init__(self, _place:str, _stamp:datetime, _samples:list[complex]):
        self._place = _place
        self. _stamp = _stamp
        self._sample= _samples

    @property
    def place(self):
        return self._place
#there was an error here not typing - befor stamp
    @property
    def stamp(self):
        return self._stamp

    @property
    def samples(self):
        return self._sample



data =  """{
    "signal": {
        "place": "Uppsala",
        "stamp": {
            "__class": "datetime",
            "y": 2025,
            "month": 4,
            "d": 19,
            "h": 16,
            "minute": 23,
            "s": 51
        },
        "samples:": [
            {
                "__class": "complex",
                "real": -2.0,
                "imag": 5.0
            },
            {
                "__class": "complex",
                "real": 3.0,
                "imag": 1.0
            },
            {
                "__class": "complex",
                "real": 2.0,
                "imag": 5.0
            }
        ]
    }
}"""


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return  { 
                     "__class":"complex",
                     "real": obj.real,
                     "imag": obj.imag
                    }
        
        return super().default(obj)
    
 
class ComplexDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=ComplexDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "complex":
            return complex(d.get("real"), d.get("imag"))

        return d

class DateTimeEncoder(json.JSONEncoder):
     
     def default(self, obj):
            if(isinstance(obj, datetime)):
                return {
                       "__class": "datetime",
                       "y": obj.year,
                       "month": obj.month,
                       "d":obj.day,
                       "h": obj.hour,
                       "minute": obj.minute,
                       "s": obj.second
                      }
          
            return json.JSONEncoder.default(self,obj) 
     
        
class DatetimeDecoder(json.JSONDecoder):
    def __init__(self):
          json.JSONDecoder.__init__(self, object_hook=DatetimeDecoder.from_dict)

    @staticmethod
    def from_dict(d):
        if d.get("__class") == "datetime":
            return datetime(d["y"],d["month"],d["d"],d["h"],d["minute"],d["s"])
                
        return d 
    

if __name__=='__main__':
    x1=json.loads(data)
    y1=json.dumps(x1["signal"]["place"])
    print(y1)
    x2 = json.loads(data, cls=ComplexDecoder)
    print(x2) 
    y2=json.dumps(x2,cls=ComplexEncoder,indent=4)

    x3=json.loads(data,cls=DatetimeDecoder)
    print(x3)
    y3=json.dumps(x3,cls=DateTimeEncoder,indent=4)

    s=Signal(x1,x2,x3)
    print(s)
