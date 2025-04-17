'''
In case we have encoded the complex number into JSON Object as list, it will not be possible to decoded or convert to pyth complex datatype
'''

import json


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return  {"complex"[obj.real, obj.imag]
        
        # In case we don't have complex object; let the base c lass default method raise the TypeError
        return super().default(obj)


        # https://stackoverflow.com/questions/71397342/how-to-use-pythons-jsondecoder
        