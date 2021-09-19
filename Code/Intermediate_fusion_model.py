#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:20:54 2019

@author: ibrahim
"""

#from keras.layers.merge import concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input, Dropout, Concatenate
from tensorflow.keras.backend import concatenate
def build_model(inp_sizes, out_size):
   models_out_list = []
   models_inp_list = []
   for i in range(len(inp_sizes)):
       model1_in = Input(shape=(inp_sizes[i],))
       model1_l1 = Dense(256, activation='relu', name='inter_layer_1_' + str(i))(model1_in)
       model1_l2 = Dropout(0.5)(model1_l1)


       inter_model = Model(model1_in, model1_l2)
       models_inp_list.append(model1_in)
       models_out_list.append(model1_l2)

   concatenated = concatenate (models_out_list)
   l1 = Dense(8192, activation='relu', kernel_initializer="he_normal", name='merged_layer_1')(concatenated)
   l2 = Dropout(0.5)(l1)
   l3 = Dense(4096, activation='relu', kernel_initializer="he_normal", name='merged_layer_2')(l2)
   l4 = Dropout(0.5)(l3)
   out = Dense(out_size, activation='linear', kernel_initializer="he_normal")(l4)
   model = Model(models_inp_list, out)
   return model
        
        
