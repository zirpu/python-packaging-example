
from __future__ import print_function, generators
import pkgutil


something = pkgutil.get_data(__name__, 'data/something.cfg')

#
#
def func():
    print("something: [{}]".format(something.strip()))
    return 42
