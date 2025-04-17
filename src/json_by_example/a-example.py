import json

"""Simple JSON <https://json.org> decoder

    Performs the following translations in decoding by default:

    +---------------+-------------------+
    | JSON          | Python            |
    +===============+===================+
    | object        | dict              |
    +---------------+-------------------+
    | array         | list              |
    +---------------+-------------------+
    | string        | str               |
    +---------------+-------------------+
    | number (int)  | int               |
    +---------------+-------------------+
    | number (real) | float             |
    +---------------+-------------------+
    | true          | True              |
    +---------------+-------------------+
    | false         | False             |
    +---------------+-------------------+
    | null          | None              |
    +---------------+-------------------+

    It also understands ``NaN``, ``Infinity``, and ``-Infinity`` as
    their corresponding ``float`` values, which is outside the JSON spec.

    """
# some JSON:

'''
{
   "name":"John",
   "age":30,
   "city":"Uppsala",
   "options":[1,3,3,4,5],
   "answers":["one","two","three"]
}

You see the last element "answer" does not end with "," see 
'''

x  ='{"name":"John", "age":30, "city": "Uppsala","options":[1,3,3,4,5],"answers":["one", "two", "three"]}'

# parse x: ( convert it to dictionary datatype)
y = json.loads(x)

# Show me some lists 
print(y["options"])
print(y["answers"])

''''
output :
[1, 3, 3, 4, 5]
['one', 'two', 'three']
'''

# show me which city 
print(y["city"])
'''
output:
Uppsala
'''
# Let us examine the type for
print(type(y['options'])) # is a list datatype
print(type(y["age"])) # is an int datatype 

# Let us convert the python dictionary type into JSON ( dumping)
x = json.dumps(y)
print(x)
'''
output:
{"name": "John", "age": 30, "city": "Uppsala", "options": [1, 3, 3, 4, 5], "answers": ["one", "two", "three"]}
'''

# let us examine the type of x 
print(type(x)) # it is str datatype ; so any dumps from python dictionary datatype make a str (string) datatype 


