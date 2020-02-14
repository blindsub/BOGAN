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
    
# BO
vt = 200
r_bo = sort_temp(tpe_function.function(vt-32, 'ackley'))

result = r_bo[:30, -1]
