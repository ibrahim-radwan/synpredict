#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:12:59 2019

@author: ibrahim
"""
import numpy as np

class DataGenerator:
    def __init__(self, label_size= 6, batch_size= 512, shuffle= True):
        self.label_size = label_size
        self.batch_size= batch_size
        self.shuffle= shuffle
    
    def __get_exploration_order(self, indexes):
        if(self.shuffle):
            np.random.shuffle(indexes)
        
        return indexes
    
    def __data_generation(self, source, target, indexes):
        
        # input
        indexes.sort()
        X = []
        for i in range(len(source)):
            s_X = source[i]['source'][list(indexes)]

            X.append(np.tanh(s_X))

        y = target['target'][list(indexes)]
        return X, y
    
    def generate(self, selected_indexes, source, target):
        # generate batches of samples
        while True:
            indexes = self.__get_exploration_order(selected_indexes)            
            # generate batches
            imax = int(len(indexes) / self.batch_size)
            for i in range(imax):
                inds = indexes[i*self.batch_size:(i+1)*self.batch_size]
                X, y = self.__data_generation(source, target, inds)
                inds = []
                yield X, y