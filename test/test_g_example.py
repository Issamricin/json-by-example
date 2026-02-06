from datetime import date, timedelta, timezone
import pytest
import json


from src.json_by_example.g_example import decode_datetime, DateTimeEncoder


@pytest.fixture
def test_data_datetime():
    return """{
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


def test_DecodeDatetime(test_data_datetime):
    decode = json.loads(test_data_datetime, object_hook=decode_datetime)
    assert isinstance(decode["report"]["created"], date)
    assert isinstance(decode["report"]["duration"], timedelta)
    assert isinstance(decode["report"]["timezone"], timezone)


def test_EncodeDatetime(test_data_datetime):
    decode = json.loads(test_data_datetime, object_hook=decode_datetime)
    encode = json.dumps(decode, cls=DateTimeEncoder)
    assert json.loads(encode) == json.loads(test_data_datetime)
