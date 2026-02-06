from datetime import date, timedelta, timezone
import json


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return {"__class": "date", "y": o.year, "month": o.month, "d": o.day}
        if isinstance(o, timedelta):
            return {
                "__class": "timedelta",
                "days": o.days,
                "seconds": o.seconds,
                "microseconds": o.microseconds,
            }
        if isinstance(o, timezone):
            offset = o.utcoffset(None).total_seconds() / 3600
            # o.utcoffset return timedelta class so we need to convert
            return {"__class": "timezone", "offset": int(offset)}
        return super().default(o)


def decode_datetime(dic):
    if dic.get("__class") == "date":
        return date(dic["y"], dic["month"], dic["d"])
    if dic.get("__class") == "timedelta":
        return timedelta(dic["days"], dic["seconds"], dic["microseconds"])
    if dic.get("__class") == "timezone":
        return timezone(timedelta(hours=dic["offset"]))
    return dic


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
ddatetime = json.loads(data, object_hook=decode_datetime)
print("Decoded :")
print(ddatetime)

edatatime = json.dumps(ddatetime, cls=DateTimeEncoder, indent=4)
print("Encoded : ")
print(edatatime)
