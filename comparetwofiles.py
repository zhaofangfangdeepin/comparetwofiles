#!/usr/bin/env python  
# -*- coding=utf-8 -*- 

import sys
import os

str1=[]
str2=[]
if len(sys.argv)!=3:
    print "Usage: %s   filename1 filename2 "%sys.argv[0]
    exit
else:
    filename1=sys.argv[1]
    filename2=sys.argv[2]
    f1=open(filename1,'r')
    f2=open(filename2,'r')
    for line in f1.readlines():
        str1.append(line)
    for line in f2.readlines():
        str2.append(line)
    a=[x for x in str1 if x in str2]
    b=[y for y in str1 if y not in str2]
    c=[z for z in str2 if z not in str1]
    for i in a:
        print "%s和%s相同的行"%(filename1,filename2)
        print i
    for i in b:
        print "在%s中不在%s中的行"%(filename1,filename2)
        print i
    for i in c:
        print "在%s中不在%s中的行"%(filename2,filename1)
        print i
