import numpy as np
from typing import Callable, List, Union

class Node:
    def __init__(self, value: Union[Callable, int, float, str], children: List['Node'] = None):
        self.value = value
        self.children = children if children else []
        if isinstance(value, (int, float)):
            self.function = lambda x: np.full_like(x, value, dtype=float)
            self.str = str(value)
        elif isinstance(value, str):
            var_split =value.split("_")
            i = int(var_split[1])
            self.function = lambda x: x[i]
            self.str = f'{var_split[0]}[{var_split[1]}]'
        else:
            self.str = f'np.{value.__name__}'
            self.function = lambda x: value(*[child.function(x) for child in self.children])
    
    def __call__(self, **kwargs) -> np.ndarray:
        return self.function(**kwargs)
    
    def __str__(self):
        return self.concat_name
        
    @property
    def concat_name(self):
        if self.is_leaf:
            return self.str
        else:
            return f'{self.str}(' + ', '.join(c.concat_name for c in self.children) + ')'

    @property
    def is_leaf(self):
        return not self.children