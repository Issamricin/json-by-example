import json

x = '''{
  "first_name": "John",
  "last_name": "Smith",
  "is_alive": true,
  "age": 27,
  "address": {
    "street_address": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postal_code": "10021-3100"
  },
  "phone_numbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [
    "Catherine",
    "Thomas",
    "Trevor"
  ],
  "spouse": null
}'''

# You can see above to preserve the format or pretty of json or to you lines, tab etc.. we use triple ''' same concept in Java we use """" 
# parse x or convert to python dictionary 

y = json.loads(x)
print(y["phone_numbers"])
# output : [{'type': 'home', 'number': '212 555-1234'}, {'type': 'office', 'number': '646 555-4567'}] 
print(type(y["phone_numbers"]))  # it is a list datatype 

# I want the first entry in the list phone_numbers
print(y["phone_numbers"][0]) #   {'type': 'home', 'number': '212 555-1234'}
print(type(y["phone_numbers"][0])) # you see it is always a dictionary datatype 

# we want the phone number for the first in the list 

print(y["phone_numbers"][0]["number"]) # 212 555-1234

# You can see so simple and powerful programming language 

# You can format the JSON object in dumps to add indentation for example 4 indentation for making JSON object pretty 

x = json.dumps(y,indent=4)
print(x)
# pretty output:
''' 
{
    "first_name": "John",
    "last_name": "Smith",
    "is_alive": true,
    "age": 27,
    "address": {
        "street_address": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postal_code": "10021-3100"
    },
    "phone_numbers": [
        {
            "type": "home",
            "number": "212 555-1234"
        },
        {
            "type": "office",
            "number": "646 555-4567"
        }
    ],
    "children": [
        "Catherine",
        "Thomas",
        "Trevor"
    ],
    "spouse": null
}

'''

x = json.dumps(y)
print(x)
# Ugly output:
''' 
{"first_name": "John", "last_name": "Smith", "is_alive": true, "age": 27, "address": {"street_address": "21 2nd Street", "city": "New York", "state": "NY", "postal_code": "10021-3100"}, "phone_numbers": [{"type": "home", "number": "212 555-1234"}, {"type": "office", "number": "646 555-4567"}], "children": ["Catherine", "Thomas", "Trevor"], "spouse": null}

'''



