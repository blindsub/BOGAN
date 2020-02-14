# -*- coding: utf-8 -*-
"""
Created on Wed Dec 4 20:26:14 2019

@author: Founder
"""

import numpy as np
import math
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
import tpe_mate

    
def function(max_time=30, func='rastrigins'):
    '''
    rastrigins、schaffer、ackley、griewank
    '''
    print("start BO!!")

    trials = Trials()

    exec("best = fmin(fn=tpe_mate."+func+", space=tpe_mate."+func+"_space, algo=tpe.suggest, max_evals=max_time, trials=trials)")
    
#    print('best:', best)
    
    res = []
    for trial in trials.trials[:]:
        temp = []
        for i in trial['misc']['vals'].values():
            temp.append(i[0])
        temp.append(trial['result']['loss'])
        res.append(temp)
#        print(trial['misc']['vals'])
#        print(trial,"\n")
    return np.array(res)
        
#r = function()