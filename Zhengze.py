# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:49:10 2018

@author: hasee_yang
"""

import re
 
ret=re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
 
print(ret.group())
print(ret.group('id'))
print(ret.group('name'))