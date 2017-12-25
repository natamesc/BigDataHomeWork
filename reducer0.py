#!/usr/bin/env python
# coding=utf-8
import sys

curKey = -10
curPRODTIME = []
meanVal = 0
for line in sys.stdin:
    items = line.split("\t")
    key = items[0] #antiNucleas
    val = items[1] #prodTime
    
    if(key==curKey or curKey ==-10):
        curKey = key
        curPRODTIME.append(float(val)) #collect prodTime
    else:
        meanVal=sum(curPRODTIME)/len(curPRODTIME)
                     
        print(curKey+"\t"+str(meanVal))

        curPRODTIME = []
        curKey = key
        curPRODTIME.append(float(val)) #collect prodTime
                    
       
meanVal=sum(curPRODTIME)/len(curPRODTIME)

print(str(curKey)+"\t"+str(meanVal))
                        
curPRODTIME = []


