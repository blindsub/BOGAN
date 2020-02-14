# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:59:01 2019

@author: founder
"""

import pandas as pd
import tensorflow as tf
import numpy as np
import math
import random
from sklearn.preprocessing import StandardScaler


def function(data, sort=False, n1=16, lam=0.06):
    # sort确定是否对输入进来的数据进行排序，默认False不排序
    tf.reset_default_graph()
    print("start igan!!!")
    tf.set_random_seed(1)  
    np.random.seed(1)
    
    # Hyper Parameters
    epoch = 40000
    BATCH_SIZE = 2 * n1       
    n2 = 16 - n1
    NumOfLine = n1
    LR_G = 0.0001           # learning rate for generator
    LR_D = 0.0001           # learning rate for discriminator
    N_IDEAS = 5             
    NumOfF = data.shape[1] 

    if sort:
        sort_key = data.shape[1] - 1
        data = pd.DataFrame(data).sort_values(ascending=True, by=[sort_key]).values[:, :-1]
        NumOfF -= 1
    
    data = data[:BATCH_SIZE, :]  
    ss = StandardScaler()
    data = ss.fit_transform(data)                        
    
    
    def sample(d1):
        if n1 == 16:
            return d1
        x = np.random.randn(n2, 10)
        d = np.vstack((d1, x))
        np.random.shuffle(d)
        return d
        
        
    def Cwork(d):       
        clist = random.sample(range(BATCH_SIZE), NumOfLine)
        datause = np.zeros(shape=(NumOfLine, NumOfF))#建立恐惧镇
        j = 0
        for c in clist:
            datause[j] = d[c]
            j = j + 1
            
        return datause
    
    
    with tf.variable_scope('Generator'):                           
        G_in = tf.placeholder(tf.float32, [None, N_IDEAS])
        G_l1 = tf.layers.dense(G_in, 128, tf.nn.relu)
        G_out = tf.layers.dense(G_l1, NumOfF)
    
    with tf.variable_scope('Discriminator'):
        real_f = tf.placeholder(tf.float32, [None, NumOfF], name='real_in') 
        D_l0 = tf.layers.dense(real_f, 128, tf.nn.relu, name='l')
        p_real = tf.layers.dense(D_l0, 1, tf.nn.sigmoid, name='out')  
        # reuse layers for generator
        D_l1 = tf.layers.dense(G_out, 128, tf.nn.relu, name='l', reuse=True)
        p_fake = tf.layers.dense(D_l1, 1, tf.nn.sigmoid, name='out', reuse=True) 
        
          
    D_loss = -tf.reduce_mean(tf.log(p_real) + tf.log(1-p_fake))
    G_loss = tf.reduce_mean(tf.log(1-p_fake))
                                                
    yy = tf.subtract(p_fake, p_real, name='yy') # (-1, 1)
    xx = tf.subtract(G_out, real_f, name='xx')  # (-1, dim)  
    gradients_node = tf.nn.tanh(tf.divide(yy, xx, name='gradients_node'))
    penaty = tf.reduce_mean(tf.square(tf.multiply(gradients_node, xx)))
    D_loss += lam * penaty
    
    
    train_D = tf.train.AdamOptimizer(LR_D).minimize(
        D_loss, var_list=tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='Discriminator'))
    train_G = tf.train.AdamOptimizer(LR_G).minimize(
        G_loss, var_list=tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='Generator'))
    
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())                     # run内参数：初始化参数的本来面目

    dll = []
    for step in range(epoch):
        dataused = sample(Cwork(data))
        G_ideas = np.random.randn(16, 5)
        G_paintings, gl, dl, gradients = sess.run([G_out, G_loss, D_loss, gradients_node, train_D, train_G],    # train and get results
                                        {G_in: G_ideas, real_f: dataused})[:4]
        
        if step % 10000 == 0:
            print('step:', step, ' G_loss:', gl, ' D_loss:', dl)
            dll.append(dl)
            
        
        if step == epoch - 2:  
            G_out_final = G_paintings
             
        if step >= epoch - 1:
            G_out_final = np.vstack((G_paintings, G_out_final))
    
    G_out_final = ss.inverse_transform(G_out_final)   
    
    print("over igan!!!")
    value_G = G_out_final
    return value_G


if __name__ == '__main__':
    data = np.array([[random.uniform(-5.12, 5.12) for i in range(5)] for j in range(300)])
    function(data)
