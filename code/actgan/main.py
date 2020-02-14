# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:58:37 2019

@author: Founder
"""

import random
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import test_function
import tpe_function
import irgan_function
import ndcg 


t_f = test_function.ackley()

def sort_temp(data):
    sort_key = data.shape[1] - 1
    data = pd.DataFrame(data).sort_values(ascending=True, by=[sort_key]).values
    return data
    

x = np.array([[random.uniform(-32.768,  32.768) for i in range(30)] for j in range(vt-32)])
r_random = sort_temp(t_f.function(x))

result_random = t_f.function(irgan_function.function(sort_temp(r_random), sort=True))
result_random = sort_temp(np.vstack((r_random, result_random)))

result = result_random[:30, -1]
