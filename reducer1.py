#!/usr/bin/env python
# coding=utf-8
import sys

curKey = -10
EF = set()
ptSum = 0
ptNum = 0

for line in sys.stdin:

    items = line.split("\t")
    key = int(items[0]) #antiNucleas
    val = items[1].split(",") #eventFile, prodTime, pt, mv
    if(key==curKey or curKey ==-10):
        curKey = key
        if float(val[1])>=float(val[3]):
            ptSum+=float(val[2])
            ptNum+=1
            EF.add(val[0])
    else:
        print(str(curKey)+"\t"+str(len(EF))+","+str(ptSum/ptNum))
        if float(val[1])>=float(val[3]):
            ptSum = float(val[2])
            ptNum = 1
            EF.clear()
            EF.add(val[0])
        curKey = key

print(str(curKey)+"\t"+str(len(EF))+","+str(ptSum/ptNum))

