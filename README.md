# Prediction of Anticancer Synergistic Combinations using Multi-Modal Deep Neural Network; Synpredict
The lack of gold standard methodology for synergy quantification of anticancer drugs warrants the consideration of different synergy metrics to develop an efficient predictive models. Furthermore, neglecting combination sensitivity may lead to biased synergistic combinations that are inefficient in conferring anticancer activity. To address this, we proposed a deep learning regression model, namely SynPredict, which effectively predicts synergy scores in Loewe, zero interaction potency (ZIP), Bliss, highest single agent (HSA), synergy score (S), and combination sensitivity score (CSS). SynPredict explored and assessed the multimodal fusion level of input data, where the gene expression data of cancer cell lines, along with the representative chemical features of drugs in pairwise combos, are processed. SynPredict variants predicted synergy and CSS scores employing the most comprehensive ONEIL and ALMANAC anticancer combination datasets to explore the effect of the data source in model performance in both intermediate and early fusion architectures of the heterogeneous input data. The empirical outcomes revealed that SynPredict outperforms the compelling DrugComb model in Bliss, HSA and ZIP synergy, with a 45-74 % decline in the mean square error (MSE). Additionally, it outperformed DeepSynergy, AuDNN synergy and TranSynergy Loewe score prediction models with a 21-34 % decline in MSE. We highlighted the impact of utilised data source, which was more significant and consistent across most synergy models compared to input data fusion architectures. Our findings demonstrated that rapid and less exhaustive in-silico predictions of drug combinations should consider a multiplex of synergy metrics and the combination sensitivity as well where the utilised dataset for model development greatly impact the subsequent performance of the model.
![image](https://user-images.githubusercontent.com/44856735/121974810-91996c80-cdc3-11eb-92d6-09401d2a46f3.png)

# Input Data
For input data, download the data files from [here](https://drive.google.com/drive/folders/1TmC5PjSCa0-oj551w758kZF2WluP6LK1?usp=sharing).

Input Files description:

1-Cell lines; list of the 76 cell lines inmplemented in SynPredict development utlising both Almanac and Oneil datasets.

2-cell_line_Gene_expression_CCLE; Gene expression data for all cell lines in CCLE database.

3-Alvadesc; physicochemical properties of drugs listed in drugComb v1.3 database (Alvadesc via OCHEM).

4-ECFP: Fingerprints of drugs listed in drugComb v1.3 database.

5-Toxalerts;toxiciphores identified in the drugs listed in drugComb v1.3 database.(Toxalerts via OCHEM).

6-Drugs_Smiles; cannonical smiles and INCHIKeys of the 4087 drugs listed in drugComb v1.3 database.

7-labels of the target score and pairwise combinations (start with dataset name either Almanac or Oniel and end with score suffix as HSA, Loewe...etc)

# Code implementation

Decompress the downloaded input folder keeping the input folder in the same folder containing the code folder will make the script running smooth

1- data preparation

Run prepare_data script after amending the input directory to specify the destination of the output data.pkl file will be generated. Just Amend the input labels_file (line 16 to the dataset and score of interest)

2- Data normalisation

Run normalise_data script utilising the data.pkl file generated from the previous step where the output .h5 sources and target will be generated


3- Training

Use either Early_fusion_model.py or Intermediate_fusion_training.py for training and nominate the directory for the output model, indices and both predicted and measure scores of the validation

# Citation 
If you used our work and found the provided data helpful please cite:


