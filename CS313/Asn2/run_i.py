# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:11:04 2012

@author: User
"""

from asn2 import main

#min_prob = 0.004
#max_prob = 0.04000001
min_prob = 0.001
max_prob = 0.004
prob_step = 0.001

seeds = [100, 200, 300, 400, 500]

#for proto in ['P', 'I', 'B', 'T']:
for proto in ['I']:
    print 'running', proto
    prob = min_prob
    while prob < max_prob:
        args = [proto, 20, prob, 50000, 5] + seeds    
        main(args)
        print 'finished prob', prob
        prob += prob_step

print 'finished sim'