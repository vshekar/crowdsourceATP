#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
print "Content-Type: application/json"

dict_of_files = {}
list_of_files = os.listdir('./problems')
for i in range(len(list_of_files)):
    dict_of_files[list_of_files[i][:-4]] = list_of_files[i]
    
print
print json.dumps(dict_of_files)   