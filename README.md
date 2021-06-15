# Prediction of Anticancer Synergistic Combinations using Multi-Modal Deep Neural Network; Synpredict
The lack of gold standard methodology for synergy quantification of anticancer drugs warrants the consideration of different synergy metrics to develop an efficient predictive models. Furthermore, neglecting combination sensitivity may lead to biased synergistic combinations that are inefficient in conferring anticancer activity. To address this, we proposed a deep learning regression model, namely SynPredict, which effectively predicts synergy scores in Loewe, zero interaction potency (ZIP), Bliss, highest single agent (HSA), synergy score (S), and combination sensitivity score (CSS). SynPredict explored and assessed the multimodal fusion level of input data, where the gene expression data of cancer cell lines, along with the representative chemical features of drugs in pairwise combos, are processed. SynPredict variants predicted synergy and CSS scores employing the most comprehensive ONEIL and ALMANAC anticancer combination datasets to explore the effect of the data source in model performance in both intermediate and early fusion architectures of the heterogeneous input data. The empirical outcomes revealed that SynPredict outperforms the compelling DrugComb model in Bliss, HSA and ZIP synergy, with a 45-74 % decline in the mean square error (MSE). Additionally, it outperformed DeepSynergy, AuDNN synergy and TranSynergy Loewe score prediction models with a 21-34 % decline in MSE. We highlighted the impact of utilised data source, which was more significant and consistent across most synergy models compared to input data fusion architectures. Our findings demonstrated that rapid and less exhaustive in-silico predictions of drug combinations should consider a multiplex of synergy metrics and the combination sensitivity as well where the utilised dataset for model development greatly impact the subsequent performance of the model.
![image](https://user-images.githubusercontent.com/44856735/121974810-91996c80-cdc3-11eb-92d6-09401d2a46f3.png)

# Input Data
For input data, download the data files from [here](https://ucstaff-my.sharepoint.com/:u:/g/personal/ibrahim_radwan_canberra_edu_au/ESMe_J-Y73JDjPKWkxgm35gBo8eT80z0Zra3U7ITzHONAg?e=DJTFP7) and decompress them.

Input Files description:

1-Cell lines; list of the 76 cell lines inmplemented in SynPredict development utlising both Almanac and Oneil datasets.

2-Cell lines_CCLE_Gene expression; Gene expression data for all cell lines in CCLE database.

3-Drugs_Alvadesc; physicochemical properties of drugs listed in drugComb v1.3 database (Alvadesc via OCHEM).

4-Drugs_ECFP: Fingerprints of drugs listed in drugComb v1.3 database.

5-Drugs_Toxalerts;toxiciphores identified in the drugs listed in drugComb v1.3 database.(Toxalerts via OCHEM).

6-Drugs_Smiles; cannonical smiles and INCHIKeys of the 4087 drugs listed in drugComb v1.3 database.

# Code implementation
1- data preparation
Run prepare_data script after amending the input directory
2- Data normalisation 

3- Training

# Citation 
If you used our work and found the provided data helpful please cite:


