#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Pool

tsvfile = "largefile.log"

def process_line(line):
    line = line.split(",")        
    key = ",".join(line[0:1])
    vector = ",".join(line[1:])
    

pool = Pool(4)
with open(tsvfile) as source_file:    
    results = pool.map(process_line, source_file, 4)


print "Succes"
