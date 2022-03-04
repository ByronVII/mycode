#!/usr/bin/env python3

import csv
import random
from os import system, name

a= "[a,b,c]"
print(a) 
print(type(a))
b= a.strip('"')
print(b)
print(type(b))
c= a.strip('][').split(',')
print(c)
print(type(c))
