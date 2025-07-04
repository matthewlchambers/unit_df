import pandas as pd
from .units import Quality

class UnitDataFrame:
    data: pd.DataFrame
    units: Quality | dict[str, Quality]

    def __init__(self, data, units):
        self.data = pd.DataFrame(data)
        self.units = units

    def __getattr__(self, name: str):
        def wrapped_attr(*args, **kwargs):
            data = getattr(self.data, name)(*args, **kwargs)
            return UnitDataFrame(data, self.units)
        match (data_attr := getattr(self.data, name)):
            case pd.DataFrame():
                return UnitDataFrame(data_attr, self.units)
            case callable(data_attr)
