class Quality:
    pass

class Length:
    base = 'foot'
    current: str
    units = {
        'foot': 1,
        'yard': 3,
        'mile': 5280
    }

    def __init__(self, unit: str):
        if unit in self.units:
            self.current = unit
        else:
            raise ValueError(f'Unsupported unit {unit} for quality {self.__class__.__name__}')
