#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:12:17 2020

@author: benji
"""


a1 = "f1e7f2cafdf93a5029b8cb8ffecf3fad74f6f80ae68169eb985a8646a69c14b5f63d7fc120c55e362b995a486165c2cfda28f3a8a05aa05d4354afced33b8773ff6d9f7a8a7517132ba8d5cb45d80bb1c25c0834c0ce"
b1 = "f2fab7c5e6ad6d5934a18c93e59a6bad74f4bd4ced9c27e1d656df12bb9914b8e0307a863a8c797e0ded7756572bcae5dd359ea39a5c844b3c45a2a1d432965ff86ce066973004240baad5b45ec346bdf3131639cbc7"


x1 = 0xf1e7f2cafdf93a5029b8cb8ffecf3fad74f6f80ae68169eb985a8646a69c14b5f63d7fc120c55e362b995a486165c2cfda28f3a8a05aa05d4354afced33b8773ff6d9f7a8a7517132ba8d5cb45d80bb1c25c0834c0ce
x2 = 0xf2fab7c5e6ad6d5934a18c93e59a6bad74f4bd4ced9c27e1d656df12bb9914b8e0307a863a8c797e0ded7756572bcae5dd359ea39a5c844b3c45a2a1d432965ff86ce066973004240baad5b45ec346bdf3131639cbc7

def xor_search(one, two, my_str, numbers=False):
    hex_str = tohex(my_str)
    k = 2*len(my_str)
    outputs = []
    for i in range(0, len(one)-k, 2):
        x1, x2 = one[i:i+k], two[i:i+k]
        x1 = int(x1, 16)
        x2 = int(x2, 16)
        outputs.append((x1 ^ x2) ^ hex_str)
        
        outputs[-1]
    
    if numbers:
        return outputs
    else:
        return list(map(hex2str, outputs))


def hex2str(my_int):
    out = hex(my_int)[2:]
    out_ints = [out[i:i+2] for i in range(0, len(out), 2)]
    return list(map(chr, map(lambda x: int(x, 16), out_ints)))

def toascii(my_str):
    return [ord(c) for c in my_str]

import binascii
def tohex(my_str):
    temp = toascii(my_str)
    return(ascii_to_int(temp))

def ascii_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def hex2intlist(my_str):
    pairs = []
    for i in range(len(my_str)//2):
        pairs.append(my_str[2*i:2*i+2])
        pairs[-1] = int(pairs[-1], 16)
    return pairs

# ascii lower case is 97 -> 122, upper case is 65 -> 90
# 44, 46 are , . respectively
# 10 is line feed
# 123, 125 are { }
# 48 - 57 are 0-9
    
import numpy as np
a = np.array(hex2intlist(a1))
b = np.array(hex2intlist(b1))
a2 = np.array(a).reshape(1, -1)
b2 = np.array(b).reshape(1, -1)

print(np.cov(np.concatenate([a2, b2])))

import matplotlib.pyplot as plt

differences = (np.abs(a-b) > 40).astype(np.int)

def get_idk(asdf):
    strs = "{:5.3}, "*10
    outputs = []
    i = 0
    j = 0
    
    def idk(k):
        return differences[k] == 0
    
    stuff1 = []
    stuff2 = []
    while 10*i + j < len(a1)//2:
        k = 10*i +j
        if idk(k):
            stuff1.append(str(asdf[k]))
            stuff2.append('')
        else:
            stuff1.append('')
            stuff2.append(str(asdf[k]))
            
        j += 1
        if j == 10:
            outputs.append(("{:5.3}, "*len(stuff1)).format(*stuff1))
            outputs.append(("{:5.3}, "*len(stuff1)).format(*stuff2))
            j = 0
            i += 1
            stuff1 = []
            stuff2 = []
            
    if not j == 10:
        outputs.append(("{:5.3}, "*len(stuff1)).format(*stuff1))
        outputs.append(("{:5.3}, "*len(stuff1)).format(*stuff2))
    
    return outputs

temp = get_idk(a)
flag_search = xor_search(a1, b1, 'flag')