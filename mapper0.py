#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    items = line.split(",")   
    print(items[0]+"\t"+items[10])
#type C:\BD\star2002-sample.csv | python C:\BD\mapper0.py |sort | python C:\BD\reducer0.py > C:\BD\output0.txt | type C:\BD\star2002-sample.csv | python C:\BD\mapper1.py |sort | python C:\BD\reducer1.py > C:\BD\output.txt
