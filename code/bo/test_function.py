# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 30:15:38 3019

@author: Founder
"""

import numpy as np
import pandas as pd
import math
# from benchmark.NeuralNetwork import nn
# from benchmark.SVM import Svm
# from benchmark.XGBoost import xgb
import sys


class base():
    def __init__(self, var=True, dim=12):
        self.var = var
        self.dim = dim
        self.min = 0.0
        self.max = 1.0
    
    def build_data(self, num, dim=12, min_=None, max_=None):
        if min_ == None:
            min_ = self.min
        if max_ == None:
            max_ = self.max
        x = np.random.uniform(min_, max_, size=(num, dim))
        return x
        
    def function(self, x):
        pass
        # 输入np.array格式的x
        # 输出np.array格式的y，如果var值为True，则输出带x，否则不带x的二维输出
    
    
class rastrigins(base):
    '''
    Description:
    Dimensions: d 
    
    The Rastrigin function has several local minima. It is highly multimodal, 
    but locations of the minima are regularly distributed.
    
    Input Domain:
    The function is usually evaluated on the hypercube xi ∈ [-5.12, 5.12], for all i = 1, …, d. 
    
    Global Minimum:
    f(x) = 0, x = (0,0...0)

    '''
    def function(self, x):
        self.dim = x.shape[1]
        ras = []
        for i in range(len(x)):
            temp = sum(map(lambda z: z**2-30*math.cos(2*math.pi*z), x[i]))
            #temp = x[i][j] ** 2 - 30 * math.cos(2*math.pi*x[i][j])
            r = 30 * self.dim + temp
            ras.append(r)
        ras = np.array(ras).reshape([-1, 1])
        if self.var:
            ras = np.hstack((x,ras))
            return ras
        else:
            return ras
        

class schaffer(base):
    '''
    Description:
    Dimensions: 2 
    
    The second Schaffer function. It is shown on a smaller input domain in the 
    second plot to show detail. 
    
    
    Input Domain:
    The function is usually evaluated on the square xi ∈ [-300, 300], for all i = 1, 2. 
    
    
    Global Minimum:
    f(x) = 0, x = (0,0...0)
    '''
    def function(self, x):
        self.dim = x.shape[1]
        if self.dim != 2:
            raise Exception("ValueError: dimtionsion error!")
        ras = []
        for i in range(len(x)):
            temp = ((math.sin(x[i][0]**2-x[i][1]**2))**2-0.5) / \
                    ((1+0.001*(x[i][0]**2+x[i][1]**2)) ** 2)
            r = 0.5 + temp
            ras.append(r)
        ras = np.array(ras).reshape([-1, 1])
        if self.var:
            ras = np.hstack((x,ras))
            return ras
        else:
            return ras
        
    
class ackley(base):
    '''
    Description:
    Dimensions: d 
    
    The Ackley function is widely used for testing optimization algorithms. 
    In its two-dimensional form, as shown in the plot above, it is characterized 
    by a nearly flat outer region, and a large hole at the centre. 
    The function poses a risk for optimization algorithms, particularly 
    hillclimbing algorithms, to be trapped in one of its many local minima. 

    Recommended variable values are: a = 30, b = 0.2 and c = 2π. 


    Input Domain:
    The function is usually evaluated on the hypercube xi ∈ [-32.768, 32.768], 
    for all i = 1, …, d, although it may also be restricted to a smaller domain.  
    
    Global Minimum:
    f(x) = 0, x = (0,0...0)

    '''
    def function(self, x):
        self.dim = x.shape[1]
        ras = []
        for i in range(len(x)):
            temp1 = sum(map(lambda z: z**2, x[i])) / self.dim
            temp2 = sum(map(lambda z: math.cos(z*2*math.pi), x[i])) / self.dim
            r = 30 + math.e - 30 * math.e ** (-0.2*math.sqrt(temp1)) - math.e ** temp2
            ras.append(r)
        ras = np.array(ras).reshape([-1, 1])
        if self.var:
            ras = np.hstack((x,ras))
            return ras
        else:
            return ras
    
    
class griewank(base):
    '''
    Description:
    Dimensions: d 
    
    The Griewank function has many widespread local minima, which are regularly distributed. 

    Input Domain:
    The function is usually evaluated on the hypercube xi ∈ [-600, 600], for all i = 1, …, d.
    
    Global Minimum:
    f(x) = 0, x = (0,0...0)

    '''
    def function(self, x):
        self.dim = x.shape[1]
        ras = []
        for i in range(len(x)):
            temp1 = sum(map(lambda z: z**2, x[i])) / 4000
            temp2 = 1
            for j in range(self.dim):
                temp2 = temp2 * math.cos(x[i][j]/(j+1))    
            r = 1 + temp1 - temp2
            ras.append(r)
        ras = np.array(ras).reshape([-1, 1])
        if self.var:
            ras = np.hstack((x,ras))
            return ras
        else:
            return ras


class NeuralNetwork():

    def function(self, x):
        ras = []
        for i in range(len(x)):
            r = nn(x[i][0], int(x[i][1]), int(x[i][2]), x[i][3], int(x[i][4]))
            ras.append(r)
        ras = np.array(ras).reshape([-1, 1])
        ras = np.hstack((x, ras))
        # print(ras)
        return ras


class SVM():
    def function(self, x):
        ras = []
        for i in range(len(x)):
            r = Svm(float(x[i][0]), x[i][1], float(x[i][2]), x[i][3])
            ras.append(r)
        ras = np.array(ras).reshape([-1, 1])
        ras = np.hstack((x, ras))
        return ras


class XGB():

    def function(self, x):
        ras = []
        for i in range(len(x)):
            r = xgb(int(x[i][0]), int(x[i][1]), x[i][2], x[i][3], int(x[i][4]))
            ras.append(r)
        ras = np.array(ras).reshape([-1, 1])

        ras = np.hstack((x, ras))
        return ras


class SumSquares():
    # xi [-5.12, 5.12]
    def function(self, x):
        dim = x.shape[1]
        ras = []
        for i in range(len(x)):
            r = 0
            for j in range(dim):
                r += (j+1) * (x[i][j] ** 2)
            ras.append(r)

        ras = np.array(ras).reshape([-1, 1])
        ras = np.hstack((x, ras))
        return ras


class zakharov():
    # xi [-5, 10]
    def function(self, x):
        dim = x.shape[1]
        ras = []
        for i in range(len(x)):
            temp1 = sum(map(lambda z: z ** 2, x[i]))
            temp2 = 0
            for j in range(dim):
                temp2 += 0.5 * (j + 1) * (x[i][j] ** 2)
            r = temp1 + temp2 ** 2 + temp2 ** 4
            ras.append(r)

        ras = np.array(ras).reshape([-1, 1])
        ras = np.hstack((x, ras))
        return ras

class dixon_price():
    # xi [-10, 10]
    def function(self, x):
        dim = x.shape[1]
        ras = []
        for i in range(len(x)):
            temp1 = (x[i][0] - 1) ** 2
            temp2 = 0
            for j in range(dim - 1):
                temp2 += (j + 2) * (2 * (x[i][j+1] ** 2) - x[i][j]) ** 2
            r = temp1 + temp2
            ras.append(r)

        ras = np.array(ras).reshape([-1, 1])
        ras = np.hstack((x, ras))
        return ras


class michalewicz():
    # xi [0, math.pi]
    def function(self, x):
        dim = x.shape[1]
        ras = []
        for i in range(len(x)):
            r = 0
            for j in range(dim):
                r += math.sin(x[i][j]) * (math.sin((j+1) * (x[i][j] ** 2) / math.pi) ** 20)
            r = -r
            ras.append(r)

        ras = np.array(ras).reshape([-1, 1])
        ras = np.hstack((x, ras))
        return ras

if __name__ == '__main__':
    bb = dixon_price()
    # a = []
    # for i in range(1, len(sys.argv)):
    #     a.append((int(sys.argv[i])))
    #
    # aa = [a]
    print(bb.function(np.array([[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]])))
