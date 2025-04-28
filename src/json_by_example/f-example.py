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


        