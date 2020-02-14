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

x = np.array([[random.uniform(-32.768,  32.768) for i in range(30)] for j in range(vt-32)])
r_random = sort_temp(t_f.function(x))

result = r_random[:30, -1]
