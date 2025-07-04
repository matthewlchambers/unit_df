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
        return UnitDataFrame(self.data.__add__(other), units=self.units)

    def __sub__(self, other):
        return UnitDataFrame(self.data.__sub__(other), units=self.units)

    def __mul__(self, other):
        return UnitDataFrame(self.data.__mul__(other), units=self.units)

    def __matmul__(self, other):
        return UnitDataFrame(self.data.__matmul__(other), units=self.units)

    def __truediv__(self, other):
        return UnitDataFrame(self.data.__truediv__(other), units=self.units)

    def __floordiv__(self, other):
        return UnitDataFrame(self.data.__floordiv__(other), units=self.units)

    def __mod__(self, other):
        return UnitDataFrame(self.data.__mod__(other), units=self.units)

    def __divmod__(self, other):
        return UnitDataFrame(self.data.__divmod__(other), units=self.units)

    def __radd__(self, other):
        return UnitDataFrame(self.data.__add__(other), units=self.units)

    def __rsub__(self, other):
        return UnitDataFrame(self.data.__sub__(other), units=self.units)

    def __rmul__(self, other):
        return UnitDataFrame(self.data.__mul__(other), units=self.units)

    def __rmatmul__(self, other):
        return UnitDataFrame(self.data.__matmul__(other), units=self.units)

    def __rtruediv__(self, other):
        return UnitDataFrame(self.data.__truediv__(other), units=self.units)

    def __rfloordiv__(self, other):
        return UnitDataFrame(self.data.__floordiv__(other), units=self.units)

    def __rmod__(self, other):
        return UnitDataFrame(self.data.__mod__(other), units=self.units)

    def __rdivmod__(self, other):
        return UnitDataFrame(self.data.__divmod__(other), units=self.units)

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
