import pytest
from datetime import datetime
from src.json_by_example.f_example import decode_data_complex, ComplexDateEncoder
import json


@pytest.fixture
def test_data_dateComplex():
    return """{
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
        "samples": [
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


def test_decodeDateComplex(test_data_dateComplex):
    decode = json.loads(test_data_dateComplex, object_hook=decode_data_complex)
    assert isinstance(decode["signal"]["stamp"], datetime)
    assert isinstance(decode["signal"]["samples"][0], complex)
    assert decode["signal"]["samples"][2] == complex(2.0, 5.0)


def test_encodeDateComplex(test_data_dateComplex):
    decode = json.loads(test_data_dateComplex, object_hook=decode_data_complex)
    encode = json.dumps(decode, cls=ComplexDateEncoder, indent=4)
    assert json.loads(encode) == json.loads(test_data_dateComplex)
