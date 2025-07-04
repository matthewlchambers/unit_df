import pandas as pd
from .units import Quality

class UnitDataFrame:
    data: pd.DataFrame
    units: Quality | dict[str, Quality]

    def __init__(self, data, units=None):
        self.data = pd.DataFrame(data)
        self.units = units

    def __repr__(self):
        return self.data.__repr__()

    def __add__(self, other):
        return self.data.__add__(other)

    def __getattr__(self, name: str):
        print(name)
        match (data_attr := getattr(self.data, name)):
            case pd.DataFrame():
                return UnitDataFrame(data_attr, self.units)
            case f if callable(data_attr):
                def wrapped_attr(*args, **kwargs):
                    data = f(*args, **kwargs)
                    return UnitDataFrame(data, self.units)
                return wrapped_attr
            case _:
                return data_attr
