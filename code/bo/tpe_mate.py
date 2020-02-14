# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:51:15 2019

@author: Founder
"""

import math
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
# from benchmark.NeuralNetwork import nn
# from benchmark.SVM import Svm
# from benchmark.XGBoost import xgb


def zakharov10(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp1 = sum(map(lambda z: z ** 2, x))
    temp2 = 0
    for j in range(dim):
        temp2 += 0.5 * (j + 1) * (x[j] ** 2)
    r = temp1 + temp2 ** 2 + temp2 ** 4
    return {'loss': r, 'status': STATUS_OK}

ras_min = -5
ras_max = 10
zakharov10_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max)
}

def zakharov30(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp1 = sum(map(lambda z: z ** 2, x))
    temp2 = 0
    for j in range(dim):
        temp2 += 0.5 * (j + 1) * (x[j] ** 2)
    r = temp1 + temp2 ** 2 + temp2 ** 4
    return {'loss': r, 'status': STATUS_OK}

ras_min = -5
ras_max = 10
zakharov30_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max),
    'x10': hp.uniform('x10', ras_min, ras_max),
    'x11': hp.uniform('x11', ras_min, ras_max),
    'x12': hp.uniform('x12', ras_min, ras_max),
    'x13': hp.uniform('x13', ras_min, ras_max),
    'x14': hp.uniform('x14', ras_min, ras_max),
    'x15': hp.uniform('x15', ras_min, ras_max),
    'x16': hp.uniform('x16', ras_min, ras_max),
    'x17': hp.uniform('x17', ras_min, ras_max),
    'x18': hp.uniform('x18', ras_min, ras_max),
    'x19': hp.uniform('x19', ras_min, ras_max),
    'x20': hp.uniform('x20', ras_min, ras_max),
    'x21': hp.uniform('x21', ras_min, ras_max),
    'x22': hp.uniform('x22', ras_min, ras_max),
    'x23': hp.uniform('x23', ras_min, ras_max),
    'x24': hp.uniform('x24', ras_min, ras_max),
    'x25': hp.uniform('x25', ras_min, ras_max),
    'x26': hp.uniform('x26', ras_min, ras_max),
    'x27': hp.uniform('x27', ras_min, ras_max),
    'x28': hp.uniform('x28', ras_min, ras_max),
    'x29': hp.uniform('x29', ras_min, ras_max)
}

def dixon_price10(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp1 = (x[0] - 1) ** 2
    temp2 = 0
    for j in range(dim - 1):
        temp2 += (j + 2) * (2 * (x[j + 1] ** 2) - x[j]) ** 2
    r = temp1 + temp2
    return {'loss': r, 'status': STATUS_OK}

ras_min = -10
ras_max = 10
dixon_price10_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max)
}

def dixon_price30(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp1 = (x[0] - 1) ** 2
    temp2 = 0
    for j in range(dim - 1):
        temp2 += (j + 2) * (2 * (x[j + 1] ** 2) - x[j]) ** 2
    r = temp1 + temp2
    return {'loss': r, 'status': STATUS_OK}

ras_min = -10
ras_max = 10
dixon_price30_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max),
    'x10': hp.uniform('x10', ras_min, ras_max),
    'x11': hp.uniform('x11', ras_min, ras_max),
    'x12': hp.uniform('x12', ras_min, ras_max),
    'x13': hp.uniform('x13', ras_min, ras_max),
    'x14': hp.uniform('x14', ras_min, ras_max),
    'x15': hp.uniform('x15', ras_min, ras_max),
    'x16': hp.uniform('x16', ras_min, ras_max),
    'x17': hp.uniform('x17', ras_min, ras_max),
    'x18': hp.uniform('x18', ras_min, ras_max),
    'x19': hp.uniform('x19', ras_min, ras_max),
    'x20': hp.uniform('x20', ras_min, ras_max),
    'x21': hp.uniform('x21', ras_min, ras_max),
    'x22': hp.uniform('x22', ras_min, ras_max),
    'x23': hp.uniform('x23', ras_min, ras_max),
    'x24': hp.uniform('x24', ras_min, ras_max),
    'x25': hp.uniform('x25', ras_min, ras_max),
    'x26': hp.uniform('x26', ras_min, ras_max),
    'x27': hp.uniform('x27', ras_min, ras_max),
    'x28': hp.uniform('x28', ras_min, ras_max),
    'x29': hp.uniform('x29', ras_min, ras_max)
}

def michalewicz10(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    r = 0
    for j in range(dim):
        r += math.sin(x[j]) * (math.sin((j + 1) * (x[j] ** 2) / math.pi) ** 20)
    r = -r
    return {'loss': r, 'status': STATUS_OK}

ras_min = 0
ras_max = math.pi
michalewicz10_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max)
}

def michalewicz30(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    r = 0
    for j in range(dim):
        r += math.sin(x[j]) * (math.sin((j + 1) * (x[j] ** 2) / math.pi) ** 20)
    r = -r
    return {'loss': r, 'status': STATUS_OK}

ras_min = 0
ras_max = math.pi
michalewicz30_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max),
    'x10': hp.uniform('x10', ras_min, ras_max),
    'x11': hp.uniform('x11', ras_min, ras_max),
    'x12': hp.uniform('x12', ras_min, ras_max),
    'x13': hp.uniform('x13', ras_min, ras_max),
    'x14': hp.uniform('x14', ras_min, ras_max),
    'x15': hp.uniform('x15', ras_min, ras_max),
    'x16': hp.uniform('x16', ras_min, ras_max),
    'x17': hp.uniform('x17', ras_min, ras_max),
    'x18': hp.uniform('x18', ras_min, ras_max),
    'x19': hp.uniform('x19', ras_min, ras_max),
    'x20': hp.uniform('x20', ras_min, ras_max),
    'x21': hp.uniform('x21', ras_min, ras_max),
    'x22': hp.uniform('x22', ras_min, ras_max),
    'x23': hp.uniform('x23', ras_min, ras_max),
    'x24': hp.uniform('x24', ras_min, ras_max),
    'x25': hp.uniform('x25', ras_min, ras_max),
    'x26': hp.uniform('x26', ras_min, ras_max),
    'x27': hp.uniform('x27', ras_min, ras_max),
    'x28': hp.uniform('x28', ras_min, ras_max),
    'x29': hp.uniform('x29', ras_min, ras_max)
}

def SumSquares10(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    r = 0
    for j in range(dim):
        r += (j + 1) * (x[j] ** 2)
    return {'loss': r, 'status': STATUS_OK}

ras_min = -5.12
ras_max = 5.12
SumSquares10_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max)
}

def SumSquares30(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    r = 0
    for j in range(dim):
        r += (j + 1) * (x[j] ** 2)
    return {'loss': r, 'status': STATUS_OK}

ras_min = -5.12
ras_max = 5.12
SumSquares30_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max),
    'x10': hp.uniform('x10', ras_min, ras_max),
    'x11': hp.uniform('x11', ras_min, ras_max),
    'x12': hp.uniform('x12', ras_min, ras_max),
    'x13': hp.uniform('x13', ras_min, ras_max),
    'x14': hp.uniform('x14', ras_min, ras_max),
    'x15': hp.uniform('x15', ras_min, ras_max),
    'x16': hp.uniform('x16', ras_min, ras_max),
    'x17': hp.uniform('x17', ras_min, ras_max),
    'x18': hp.uniform('x18', ras_min, ras_max),
    'x19': hp.uniform('x19', ras_min, ras_max),
    'x20': hp.uniform('x20', ras_min, ras_max),
    'x21': hp.uniform('x21', ras_min, ras_max),
    'x22': hp.uniform('x22', ras_min, ras_max),
    'x23': hp.uniform('x23', ras_min, ras_max),
    'x24': hp.uniform('x24', ras_min, ras_max),
    'x25': hp.uniform('x25', ras_min, ras_max),
    'x26': hp.uniform('x26', ras_min, ras_max),
    'x27': hp.uniform('x27', ras_min, ras_max),
    'x28': hp.uniform('x28', ras_min, ras_max),
    'x29': hp.uniform('x29', ras_min, ras_max)
}

def rastrigins10(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp = sum(map(lambda z: z**2-10*math.cos(2*math.pi*z), x))
    r = 10 * dim + temp
    return {'loss': r, 'status': STATUS_OK}

ras_min = -5.12
ras_max = 5.12
rastrigins10_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max)
}


def rastrigins30(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp = sum(map(lambda z: z**2-10*math.cos(2*math.pi*z), x))
    r = 10 * dim + temp
    return {'loss': r, 'status': STATUS_OK}

ras_min = -5.12
ras_max = 5.12
rastrigins30_space = {
    'x0': hp.uniform('x0', ras_min, ras_max),
    'x1': hp.uniform('x1', ras_min, ras_max),
    'x2': hp.uniform('x2', ras_min, ras_max),
    'x3': hp.uniform('x3', ras_min, ras_max),
    'x4': hp.uniform('x4', ras_min, ras_max),
    'x5': hp.uniform('x5', ras_min, ras_max),
    'x6': hp.uniform('x6', ras_min, ras_max),
    'x7': hp.uniform('x7', ras_min, ras_max),
    'x8': hp.uniform('x8', ras_min, ras_max),
    'x9': hp.uniform('x9', ras_min, ras_max),
    'x10': hp.uniform('x10', ras_min, ras_max),
    'x11': hp.uniform('x11', ras_min, ras_max),
    'x12': hp.uniform('x12', ras_min, ras_max),
    'x13': hp.uniform('x13', ras_min, ras_max),
    'x14': hp.uniform('x14', ras_min, ras_max),
    'x15': hp.uniform('x15', ras_min, ras_max),
    'x16': hp.uniform('x16', ras_min, ras_max),
    'x17': hp.uniform('x17', ras_min, ras_max),
    'x18': hp.uniform('x18', ras_min, ras_max),
    'x19': hp.uniform('x19', ras_min, ras_max),
    'x20': hp.uniform('x20', ras_min, ras_max),
    'x21': hp.uniform('x21', ras_min, ras_max),
    'x22': hp.uniform('x22', ras_min, ras_max),
    'x23': hp.uniform('x23', ras_min, ras_max),
    'x24': hp.uniform('x24', ras_min, ras_max),
    'x25': hp.uniform('x25', ras_min, ras_max),
    'x26': hp.uniform('x26', ras_min, ras_max),
    'x27': hp.uniform('x27', ras_min, ras_max),
    'x28': hp.uniform('x28', ras_min, ras_max),
    'x29': hp.uniform('x29', ras_min, ras_max)
}


def schaffer(params):
    x = []
    for i in params.values():
        x.append(i)
    temp = ((math.sin(x[0]**2-x[1]**2))**2-0.5) / \
                    ((1+0.001*(x[0]**2+x[1]**2)) ** 2)
    r = 0.5 + temp
    return {'loss': r, 'status': STATUS_OK}

schaffer_space = {
    'x0': hp.uniform('x0', -100, 100),
    'x1': hp.uniform('x1', -100, 100)}


def ackley10(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp1 = sum(map(lambda z: z**2, x)) / dim
    temp2 = sum(map(lambda z: math.cos(z*2*math.pi), x)) / dim
    r = 20 + math.e - 20 * math.e ** (-0.2*math.sqrt(temp1)) - math.e ** temp2
    return {'loss': r, 'status': STATUS_OK}

ack_min = -32.768
ack_max = 32.768
ackley10_space = {
    'x0': hp.uniform('x0', ack_min, ack_max),
    'x1': hp.uniform('x1', ack_min, ack_max),
    'x2': hp.uniform('x2', ack_min, ack_max),
    'x3': hp.uniform('x3', ack_min, ack_max),
    'x4': hp.uniform('x4', ack_min, ack_max),
    'x5': hp.uniform('x5', ack_min, ack_max),
    'x6': hp.uniform('x6', ack_min, ack_max),
    'x7': hp.uniform('x7', ack_min, ack_max),
    'x8': hp.uniform('x8', ack_min, ack_max),
    'x9': hp.uniform('x9', ack_min, ack_max)
}


def ackley30(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp1 = sum(map(lambda z: z**2, x)) / dim
    temp2 = sum(map(lambda z: math.cos(z*2*math.pi), x)) / dim
    r = 20 + math.e - 20 * math.e ** (-0.2*math.sqrt(temp1)) - math.e ** temp2
    return {'loss': r, 'status': STATUS_OK}

ack_min = -32.768
ack_max = 32.768
ackley30_space = {
    'x0': hp.uniform('x0', ack_min, ack_max),
    'x1': hp.uniform('x1', ack_min, ack_max),
    'x2': hp.uniform('x2', ack_min, ack_max),
    'x3': hp.uniform('x3', ack_min, ack_max),
    'x4': hp.uniform('x4', ack_min, ack_max),
    'x5': hp.uniform('x5', ack_min, ack_max),
    'x6': hp.uniform('x6', ack_min, ack_max),
    'x7': hp.uniform('x7', ack_min, ack_max),
    'x8': hp.uniform('x8', ack_min, ack_max),
    'x9': hp.uniform('x9', ack_min, ack_max),
    'x10': hp.uniform('x10', ack_min, ack_max),
    'x11': hp.uniform('x11', ack_min, ack_max),
    'x12': hp.uniform('x12', ack_min, ack_max),
    'x13': hp.uniform('x13', ack_min, ack_max),
    'x14': hp.uniform('x14', ack_min, ack_max),
    'x15': hp.uniform('x15', ack_min, ack_max),
    'x16': hp.uniform('x16', ack_min, ack_max),
    'x17': hp.uniform('x17', ack_min, ack_max),
    'x18': hp.uniform('x18', ack_min, ack_max),
    'x19': hp.uniform('x19', ack_min, ack_max),
    'x20': hp.uniform('x20', ack_min, ack_max),
    'x21': hp.uniform('x21', ack_min, ack_max),
    'x22': hp.uniform('x22', ack_min, ack_max),
    'x23': hp.uniform('x23', ack_min, ack_max),
    'x24': hp.uniform('x24', ack_min, ack_max),
    'x25': hp.uniform('x25', ack_min, ack_max),
    'x26': hp.uniform('x26', ack_min, ack_max),
    'x27': hp.uniform('x27', ack_min, ack_max),
    'x28': hp.uniform('x28', ack_min, ack_max),
    'x29': hp.uniform('x29', ack_min, ack_max)
}

def griewank10(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp1 = sum(map(lambda z: z**2, x)) / 4000
    temp2 = 1
    for j in range(dim):
        temp2 = temp2 * math.cos(x[j]/(j+1))    
    r = 1 + temp1 - temp2
    return {'loss': r, 'status': STATUS_OK}

gri_min = -600
gri_max = 600
griewank10_space = {
    'x0': hp.uniform('x0', gri_min, gri_max),
    'x1': hp.uniform('x1', gri_min, gri_max),
    'x2': hp.uniform('x2', gri_min, gri_max),
    'x3': hp.uniform('x3', gri_min, gri_max),
    'x4': hp.uniform('x4', gri_min, gri_max),
    'x5': hp.uniform('x5', gri_min, gri_max),
    'x6': hp.uniform('x6', gri_min, gri_max),
    'x7': hp.uniform('x7', gri_min, gri_max),
    'x8': hp.uniform('x8', gri_min, gri_max),
    'x9': hp.uniform('x9', gri_min, gri_max)
}


def griewank30(params):
    x = []
    for i in params.values():
        x.append(i)
    dim = len(x)
    temp1 = sum(map(lambda z: z**2, x)) / 4000
    temp2 = 1
    for j in range(dim):
        temp2 = temp2 * math.cos(x[j]/(j+1))
    r = 1 + temp1 - temp2
    return {'loss': r, 'status': STATUS_OK}

gri_min = -600
gri_max = 600
griewank30_space = {
    'x0': hp.uniform('x0', gri_min, gri_max),
    'x1': hp.uniform('x1', gri_min, gri_max),
    'x2': hp.uniform('x2', gri_min, gri_max),
    'x3': hp.uniform('x3', gri_min, gri_max),
    'x4': hp.uniform('x4', gri_min, gri_max),
    'x5': hp.uniform('x5', gri_min, gri_max),
    'x6': hp.uniform('x6', gri_min, gri_max),
    'x7': hp.uniform('x7', gri_min, gri_max),
    'x8': hp.uniform('x8', gri_min, gri_max),
    'x9': hp.uniform('x9', gri_min, gri_max),
    'x10': hp.uniform('x10', gri_min, gri_max),
    'x11': hp.uniform('x11', gri_min, gri_max),
    'x12': hp.uniform('x12', gri_min, gri_max),
    'x13': hp.uniform('x13', gri_min, gri_max),
    'x14': hp.uniform('x14', gri_min, gri_max),
    'x15': hp.uniform('x15', gri_min, gri_max),
    'x16': hp.uniform('x16', gri_min, gri_max),
    'x17': hp.uniform('x17', gri_min, gri_max),
    'x18': hp.uniform('x18', gri_min, gri_max),
    'x19': hp.uniform('x19', gri_min, gri_max),
    'x20': hp.uniform('x20', gri_min, gri_max),
    'x21': hp.uniform('x21', gri_min, gri_max),
    'x22': hp.uniform('x22', gri_min, gri_max),
    'x23': hp.uniform('x23', gri_min, gri_max),
    'x24': hp.uniform('x24', gri_min, gri_max),
    'x25': hp.uniform('x25', gri_min, gri_max),
    'x26': hp.uniform('x26', gri_min, gri_max),
    'x27': hp.uniform('x27', gri_min, gri_max),
    'x28': hp.uniform('x28', gri_min, gri_max),
    'x29': hp.uniform('x29', gri_min, gri_max)
}


def nn_tpe(params):
    x = []
    for i in params.values():
        x.append(i)
    r = nn(x[0], x[1], x[2], x[3], x[4])
    return {'loss': r, 'status': STATUS_OK}

nn_tpe_space = {
    'x0': hp.uniform('x0', 0.01, 1),
    'x1': hp.randint('x1', 126) + 2,
    'x2': hp.randint('x2', 126) + 2,
    'x3': hp.uniform('x3', 0.1, 1),
    'x4': hp.randint('x4', 31) + 1
}

def svm_tpe(params):
    x = []
    for i in params.values():
        x.append(i)
    r = Svm(x[0], x[1], x[2], x[3])
    return {'loss': r, 'status': STATUS_OK}

svm_tpe_space = {
    'x0': hp.uniform('x0', 0, 20),
    'x1': hp.choice('x1', ['linear', 'sigmoid', 'poly', 'rbf']),
    'x2': hp.uniform('x2', 0, 20),
    'x3': hp.choice('x3', ['ovr', 'ovo'])
}

def xgb_tpe(params):
    x = []
    for i in params.values():
        x.append(i)

    r = xgb(x[0], x[1], x[2], x[3], x[4])
    return {'loss': r, 'status': STATUS_OK}

xgb_tpe_space = {
    "x0": hp.randint("x0", 15) + 5,
    "x1": hp.randint("x1", 300) + 150,
    'x2': hp.uniform('x2', 1e-3, 5e-1) * 0.02 + 0.05,
    "x3": hp.randint("x3", 5) * 0.1 + 0.5,
    "x4": hp.randint("x4", 6) + 1,
}