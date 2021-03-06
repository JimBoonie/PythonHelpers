"""
Short test code for demonstrating the difference between several ways of
listing the path to the file in which a class was defined.
"""

import sys

class PathList:
  def __init__(self):
    print(self.__class__.__module__)
    print(sys.modules[self.__class__.__module__])
    print(sys.modules[self.__class__.__module__].__file__)

if __name__ == '__main__':
  a = PathList()

