#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 08:48:29 2019
Normalize data
@author: ibrahim
"""

import pickle
import h5py as h5
import numpy as np

# load data
dirpath = '../input/'
data_file = dirpath + 'data.pkl'
with open(data_file, 'rb') as f:
    data = pickle.load(f)

print(len(data))

# concatenate all features as the source matrix, the same for the labels
source = []
target = []


for key in data[0].keys():
    print(key)
    if key == 'label':
        continue
    for sample in data:
        temp = sample[key]
#        if len(source) == 0:
#            source = temp
#        else:
        source.append(temp)
            
    ## Normalize
    source = np.array(source, dtype='float32')
    print(source.shape)
    means = []
    stds = []
    for i in range(source.shape[1]):
        mean = np.mean(source[:,i])
        std = np.std(source[:,i])
        means.append(mean)
        stds.append(std)    
    
    filtered_feats = [j for j , e in enumerate(stds) if e != 0]
    source = source[:, filtered_feats]
    means = [means[filtered_feats[j]] for j in range(len(filtered_feats))]
    stds = [stds[filtered_feats[j]] for j in range(len(filtered_feats))]
    # save
    file_name = dirpath + '/source_' + key + '.h5'
    hf = h5.File(file_name, 'w')
#    source = pca_transform(source)
    hf.create_dataset('source', data= source)
    hf.create_dataset('means', data= means)
    hf.create_dataset('stds', data= stds)
    hf.close()
    print(source.shape)
    source = []
    means = []
    stds = []



target = []
for sample in data:
    temp = sample['label']

    target.append(temp)
target = np.array(target, dtype='float32')
file_name = dirpath + '/target.h5'
hf = h5.File(file_name, 'w')
hf.create_dataset('target', data= target)
hf.close()
target = []
    