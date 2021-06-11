#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:23:19 2019

@author: ibrahim
"""

import pandas as pd
import numpy as np
import pickle
import os

print("CWD: " + os.getcwd() )
dirpath = '../data4/bliss/'
labels_file = dirpath + "Almanac_dc_v1.3_bliss.csv"
chem_disc_file_tx = dirpath + "Toxalerts.csv"
chem_disc_file_ecfp = dirpath + "ECFP.csv"
chem_disc_file_pydes = dirpath + "Alvadesc.csv"
sc_gene_exp_file = dirpath + "CCLE_GE_gene_attribute_matrix_standardized.csv"


# read data
labels = pd.read_csv(labels_file)
print(labels.shape)

chem_disc_tx = pd.read_csv(chem_disc_file_tx)
print(chem_disc_tx.shape)

chem_disc_ecfp = pd.read_csv(chem_disc_file_ecfp)
print(chem_disc_ecfp.shape)

chem_disc_pydes = pd.read_csv(chem_disc_file_pydes)
print(chem_disc_pydes.shape)

sc_gene_exp = pd.read_csv(sc_gene_exp_file)
print(sc_gene_exp.shape)

length = labels.shape[0]

Data = []
for i in range(length):
    drugA_name = labels.iloc[i,0]
    if drugA_name not in chem_disc_tx.columns:
        continue
    drugA_feat_tx = chem_disc_tx[drugA_name]
    drugA_feat_ecfp = chem_disc_ecfp[drugA_name]
    drugA_feat_pydes = chem_disc_pydes[drugA_name]
    drugB_name = labels.iloc[i,1]
    if drugB_name not in chem_disc_tx.columns:
        continue
    drugB_feat_tx = chem_disc_tx[drugB_name]
    drugB_feat_ecfp = chem_disc_ecfp[drugB_name]
    drugB_feat_pydes = chem_disc_pydes[drugB_name]
    
    
    cell_line_name = labels.iloc[i, 2]
    if cell_line_name not in sc_gene_exp.columns:
        continue
    cell_line_feat_scores = sc_gene_exp[cell_line_name]

    label = labels.iloc[i, 3]
    
    # create a dictionary for each sample
    sample = dict()
    sample['drugA_tx'] = drugA_feat_tx
    sample['drugA_ecfp'] = drugA_feat_ecfp
    sample['drugA_alvades'] = drugA_feat_pydes
    sample['drugB_tx'] = drugB_feat_tx
    sample['drugB_ecfp'] = drugB_feat_ecfp
    sample['drugB_alvades'] = drugB_feat_pydes
    sample['cellLineSC'] = cell_line_feat_scores

    sample['label'] = label
    
    print(i)
    Data.append(sample)
# save data into disk for latter usage
output_file = dirpath + '/data.pkl'
with open(output_file, 'wb') as f:
   pickle.dump(Data, f)
