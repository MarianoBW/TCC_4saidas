#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 12:12:31 2018

@author: marianobw
"""

#import random
import statistics
             #  1,1,3,3,4,5,6,7,9
data_points = [ 1,4,5,6,1,7,3,9,3]
diftempo=statistics.median(data_points)
print '\ndiferenca tempo mediana =%s '%(diftempo)