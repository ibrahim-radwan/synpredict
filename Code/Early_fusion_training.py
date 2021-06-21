#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 15:37:21 2019

@author: ibrahim
"""


import numpy as np
import h5py
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
import tensorflow.keras as K

from data_generator_ef import DataGenerator
from Early_fusion_model import build_model
from keras.models import model_from_json, Model

from reset_keras import reset_keras
from keras.layers import Dense


def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def pop_layer(model):
    if not model.outputs:
        raise Exception('Sequential model cannot be popped: model is empty.')

    model.layers.pop()
    if not model.layers:
        model.outputs = []
        model.inbound_nodes = []
        model.outbound_nodes = []
    else:
        model.layers[-1].outbound_nodes = []
        model.outputs = [model.layers[-1].output]
    model.built = False


# read data
dirpath = '../input/'
# source
source_drugA_tx = h5py.File(dirpath + '/source_drugA_tx.h5', 'r')
source_drugA_ecfp = h5py.File(dirpath + '/source_drugA_ecfp.h5', 'r')
source_drugA_pydes = h5py.File(dirpath + '/source_drugA_alvades.h5', 'r')
source_drugB_tx = h5py.File(dirpath + '/source_drugB_tx.h5', 'r')
source_drugB_ecfp = h5py.File(dirpath + '/source_drugB_ecfp.h5', 'r')
source_drugB_pydes = h5py.File(dirpath + '/source_drugB_alvades.h5', 'r')
source_cellLineSC = h5py.File(dirpath + '/source_cellLineSC.h5', 'r')

# labels
target = h5py.File(dirpath + 'target.h5', 'r')

# setup folds for training/validation/testing'
nFolds = 5
kf = KFold(n_splits=5)
length = target['target'].shape[0]
indecies = range(length)
train_indices = []
test_indices = []
for train_index, test_index in kf.split(indecies):
    train_indices.append(train_index)
    test_indices.append(test_index)
del indecies

mse = []

for fold_i in range(nFolds):


    # load data
    params_train = {
            'label_size': 1,
            'batch_size': 32,
            'shuffle': True
            }


    params_valid = {
            'label_size': 1,
            'batch_size': 32,
            'shuffle': False
            }
    
    params_predict = {
            'label_size': 1,
            'batch_size': 1,
            'shuffle': False
            }

#    batch_size_predicted = 32

    list_of_sources = [source_drugA_tx, source_drugA_ecfp, source_drugA_pydes, source_drugB_tx, source_drugB_ecfp, source_drugB_pydes, source_cellLineSC]



    training_generator = DataGenerator(**params_train).generate(train_indices[fold_i], list_of_sources, target)
    testing_generator = DataGenerator(**params_valid).generate(test_indices[fold_i], list_of_sources, target)

    # build model
    out_size = 1
    inp_sizes = []
    inp = 0
    for i in range(len(list_of_sources)):
        inp_sizes.append(list_of_sources[i]['source'].shape[1])
        inp = inp + list_of_sources[i]['source'].shape[1]

    model2 = build_model(inp, out_size)



    # train for hyper paramters
    NUM_EPOCHS = 2
    model2.compile(loss='mean_squared_error', optimizer=K.optimizers.SGD(lr=0.00001,momentum=0.5), metrics=["mse"])
    print(model2.summary())

    earlyStopping = K.callbacks.EarlyStopping(monitor='val_loss', patience=200, verbose=1, mode='auto')

    H = model2.fit_generator(generator = training_generator,
                        steps_per_epoch = len(train_indices[fold_i])//params_train['batch_size'],
                        validation_data = testing_generator,
                        validation_steps = len(test_indices[fold_i])//params_valid['batch_size'],
                        epochs= NUM_EPOCHS,
                        callbacks=[earlyStopping],
                        verbose= 1) #1 print everystep 2 print epoch 0 no print

    test_loss = H.history['val_loss']
    
    predicting_generator = DataGenerator(**params_predict).generate(test_indices[fold_i], list_of_sources, target)
    predicted_scores = model2.predict_generator(predicting_generator, steps=len(test_indices[fold_i]))
    print(predicted_scores.shape)

    model2.reset_states()

    # N = len(H.history["loss"])
    # plt.style.use("ggplot")
    # plt.figure()
    # plt.plot(np.arange(0, N), H.history["loss"], label="train_loss")
    # plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
    # plt.plot(np.arange(0, N), H.history["mean_squared_error"], label="train_mse")
    # plt.plot(np.arange(0, N), H.history["val_mean_squared_error"], label="val_mse")
    # plt.title("Training Loss and mean squared error on Dataset")
    # plt.xlabel("Epoch #")
    # plt.ylabel("Loss/MSE")
    # plt.legend(loc="lower left")
    # plt.savefig("plot.png")

    # save model
    model_json = model2.to_json()
    model_name_json = '../model' + str(fold_i) + '.json'
    with open(model_name_json, 'w') as json_file:
     json_file.write(model_name_json)


    model_name_h5 = '../model_fold_' + str(fold_i) + '.h5'
    model2.save_weights(model_name_h5)

    # save indecises
    train_inds_name = '../model_train_inds_' + str(fold_i) + '.npy'
    np.save(train_inds_name, train_indices[fold_i])

    test_inds_name = '../model_test_inds_' + str(fold_i) + '.npy'
    np.save(test_inds_name, test_indices[fold_i])
    print(test_loss[-1])
    mse.append(test_loss[-1])
    reset_keras()

    # save prediction and labels of this fold
    test_inds = test_indices[fold_i]
    test_inds.sort()

    exp_scores = target['target'][list(test_inds)]
    np.savetxt('../model_target_' + str(fold_i) + '.csv', exp_scores, delimiter=',')

    np.savetxt('../model_predicted_' + str(fold_i) + '.csv', predicted_scores, delimiter=',')

