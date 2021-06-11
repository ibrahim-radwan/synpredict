#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:20:54 2019

@author: ibrahim
"""

from keras.layers.merge import concatenate
from keras.models import Model
from keras.layers import Dense, Input, Dropout

def build_model(inp_sizes, out_size):

    model1_in = Input(shape=(inp_sizes,))
    l1 = Dense(8182, activation='relu', kernel_initializer="he_normal", name='merged_layer_1')(model1_in)
    l2 = Dropout(0.5)(l1)
    l3 = Dense(4096, activation='relu', kernel_initializer="he_normal", name='merged_layerdsfssad2')(l2)
    l4 = Dropout(0.5)(l3)
    out = Dense(out_size, activation='linear', kernel_initializer="he_normal")(l4)
    model = Model(model1_in, out)
    return model
        
        