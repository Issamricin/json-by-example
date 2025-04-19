'''
The Python json.JSONEncoder.iterencode() method is a method of the json.JSONEncoder class that encodes a Python object into a JSON-formatted string. 
It returns an iterator that yields the encoded string in chunks.

This method is useful when dealing with large datasets, as it avoids creating a single large JSON string in memory.
Parameters
This method accepts the Python object as a parameter that needs to be serialized into a JSON-formatted string.

Return Value
This method returns an iterator that yields the JSON-formatted string in chunks instead of returning it as a whole.

'''

import json

# Create an instance of JSONEncoder
encoder = json.JSONEncoder()

# Sample dictionary
data = {"name": "Alice", "age": 25, "city": "London"}

# Encode JSON in chunks using iterencode()
json_iterator = encoder.iterencode(data)

# Print each chunk
print("JSON Output:")
for chunk in json_iterator:
   print(chunk, end="")

   # dictionary convert to real JSON 
   #  {"name": "Alice", "age": 25, "city": "London"} 

# use tuple 
print(" START\n")
data = ("alan", 1, 2, True)
json_iterator = encoder.iterencode(data)
for chunk in json_iterator:
   print(chunk)

# tuple convert to a list which is correct see "True" become "true"
'''
["alan"
, 1
, 2
, true
]


'''  


   