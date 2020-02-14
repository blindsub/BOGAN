# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:32:27 2019

@author: Founder
"""

import math
import numpy as np
import copy
from sklearn.preprocessing import MinMaxScaler


def IDCG(n, length=0):
    n = sorted(n)
    idcg = 0
    if length ==0:
        length = len(n)

    for i in range(length):
        idcg += (2 ** (-n[i])) / math.log(i + 2, 2)
        # idcg += (100 - n[i]) / math.log(i + 2, 2)
    return idcg

def DCG(data, index):
    dcg = 0
    for i in range(len(data)):
        t = (2 ** (-data[i])) / math.log(index[i] + 2, 2)
#        print(t)
        dcg += t
    return dcg


def nDCG2(d1, d2):
    d1 = sorted(list(d1))
    d2 = sorted(list(d2))

    if d1[0] <= d2[0]:
        jihe = 0
    else:
        jihe = 1

    ddd = []
    index1 = []; index2 = []
    i = 0; j = 0; index = 0
    while i < len(d1) and j < len(d2):
        if d1[i] <= d2[j]:
            ddd.append(d1[i])
            index1.append(index)
            i += 1
        else:
            ddd.append(d2[j])
            index2.append(index)
            j += 1
        index += 1
    while i < len(d1):
        ddd.append(d1[i])
        index1.append(index)
        i += 1
        index += 1
    while j < len(d2):
        ddd.append(d2[j])
        index2.append(index)
        j += 1
        index += 1
    del d1, d2
    
    ddd = np.array(ddd).reshape(-1, 1)
    ss = MinMaxScaler((0, 10))
    ddd = ss.fit_transform(ddd)
    ddd = list(ddd.reshape(-1))
    d1 = []; d2 = []
    for i in index1:
        d1.append(ddd[i])
    for i in index2:
        d2.append(ddd[i])
    
    dd = IDCG(ddd, len(d2))

    return (IDCG(d2) / dd)/(IDCG(d1) / dd), jihe


def nDCG(data):
    n = len(data); index = []; data_ss = []
    for i  in range(n):
        data[i] = sorted(list(data[i]))
        index.append([])
        data_ss.append([])
    
    def select_small(data):
        temp = float('Inf'); index = 0
        for i in range(len(data)):
            if len(data[i]) != 0:
                if data[i][0] < temp:
                    temp = data[i][0]
                    index = i
        data[index].pop(0)
        return data, temp, index
    
    
    def null_determine(data):
        add = 0
        for i in range(len(data)):
            add += len(data[i])
        if add == 0:
            return True
        return False
    
    ddd = []
    index_ddd = 0
    while 1:
        if null_determine(data):
            break
        data, temp, index_index = select_small(data)
        ddd.append(temp)
        index[index_index].append(index_ddd)
        index_ddd += 1
    
    ddd = np.array(ddd).reshape(-1, 1)
    ss = MinMaxScaler((0, 1))
    ddd = ss.fit_transform(ddd)
    ddd = list(ddd.reshape(-1))
    
    index_i = []; index_ = []
    for i in range(30):
        index_i.append(i)
        index_.append(i+index_ddd-30)
    dcg_i = DCG(ddd[: 30], index_i)
    dcg_ = DCG(ddd[-30: ], index_)
    
    for i in range(n):
        for j in range(len(index[i])):
            data_ss[i].append(ddd[index[i][j]])

    ndcg = []
    for i in range(n):
        temp = DCG(data_ss[i], index[i])
        ndcg.append((temp-dcg_)/(dcg_i-dcg_))

    return ndcg
       
        
if __name__ == "__main__":
#    print((0.5+1/(4*math.log(3, 2))+1/16)/(0.5+1/(2*math.log(3, 2))+1/4))