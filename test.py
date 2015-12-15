# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 20:31:57 2015

@author: Kennard
"""

eol = b'\r'
leneol = len(eol)

line = bytearray()

line += b'0.09080983761'
line += eol
line += b'789.098767831'
line += eol
line += b'2.09837676831'
line += eol
line += b'3429.08767831'
line += eol

val = bytearray()

tst = b'abcdefgh' + eol + b'qwerty' + eol + b'hallo' + eol + b'neejamisschien' + eol


i = 0
while i < len(tst):
    if tst[i:i+leneol] == eol:
        val = tst[:i]
        print(val)
        
        tst = tst[i+leneol:]
        i = 0
        
    
    i +=1