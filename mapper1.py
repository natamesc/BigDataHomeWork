#!/usr/bin/env python
# coding=utf-8
import sys

f = open('C:\BD\output0.txt', 'r')
mv = dict()
for line in f:
    line = line.rstrip('\n')
    val = line.split("\t")
    mv[val[0]]=val[1]
f.close()

mv
for line in sys.stdin:
    items = line.split(",")   
    print(items[0]+"\t"+items[1]+","+items[10]+","+items[11]+','+mv[items[0]])
    
#type C:\BD\star2002-sample.csv | python C:\BD\mapper0.py |sort | python C:\BD\reducer0.py > C:\BD\output0.txt
#type C:\BD\star2002-sample.csv | python C:\BD\mapper1.py |sort | python C:\BD\reducer1.py > C:\BD\output.txt
