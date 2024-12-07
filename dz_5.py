import inspect

import colorama
print(callable(colorama))
print(colorama,__name__)
print(inspect.ismodule(colorama))
print(inspect.iscode(colorama))
print(inspect.isclass(colorama))
print(inspect.getmodule(colorama))
print(colorama,__doc__)
print(colorama,__file__)


