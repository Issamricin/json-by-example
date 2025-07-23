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
        return self._samples



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


class complexencoder(json.JSONEncoder): 
    def defualt(self,obj):
        if isinstance(obj,complex):
            return{'__class':'complex',
                   "real":obj.real,
                   "imag":obj.imag}
        return super().default(obj)
        
class complexdecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self,object_hook=complexdecoder.from_dict)

        @staticmethod
        def from_dict(d):
            if d.get("__class")=="complex":
                return complex(d.get("real"),d.get("imag"))
            return d

class datatimeencoder(json.JSONEncoder):
    def default(self, obj):
        if (isinstance(obj,datetime)):
            return{
                "__class":"datatime",
                "y":obj.year,
                "month":obj.month,
                "day":obj.day,
                "H":obj.hour,
                "M":obj.minute,
                "S":obj.second
            }
        return json.JSONEncoder.default(self,obj)
    
class datatimedecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self,object_hook=datatimedecoder.from_dict)

    def from_dict(d):
        if d.get("__class")=="datatime":
            return datetime(d["y"],d["month"],d["day"],d["H"],d["M"],d["S"])
        return d


if __name__=='__main__':
    
    d_data=json.loads(data)
 
    a=d_data["signal"]["samples:"] #typr str
    x_complex=list(json.dumps(a,cls=complexencoder))
    print(type(x_complex))
    stamp=datetime.now()
    x_datetime=json.dumps(stamp,cls=datatimeencoder)
    print(x_datetime)
    
    datetimedec=json.loads(x_datetime,cls=datatimedecoder)
    print(datetimedec)
    print(type(datetimedec))
    
    s=Signal(d_data["signal"]["place"],datetimedec,x_complex)
    print("class signal:\n",s.place)
    print("class signal \n",s.stamp)
    print("class signal \n",s._sample)