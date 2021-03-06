# Prediction of Anticancer Synergistic Combinations using Multi-Modal Deep Neural Network; SynPredict
The lack of gold standard methodology for synergy quantification of anticancer drugs warrants the consideration of different synergy metrics to develop efficient Artificial Intelligence-based predictive methods. Furthermore, neglecting combination sensitivity in synergy prediction may lead to biased synergistic combinations that are inefficient in conferring anticancer activity. To address this, we proposed a deep learning model, namely SynPredict, which can effectively predict synergy scores in Loewe, zero interaction potency (ZIP), Bliss, highest single agent (HSA), synergy score (S), and combination sensitivity score (CSS). SynPredict explored and assessed the multimodal fusion level of input data, including the gene expression data of cancer cells, along with the representative chemical features of drugs in pairwise combos. SynPredict variants predicted synergy and CSS scores employing the most comprehensive ONEIL and ALMANAC anticancer combination datasets to explore the effect of the data source in model performance in both intermediate and early fusion architectures of the heterogeneous input data. The empirical outcomes revealed that SynPredict outperformed the compelling DrugComb model in Bliss, HSA and ZIP synergy, with a 45-74\% decline in the mean square error (MSE). Additionally, it surpassed DeepSynergy, AuDNN synergy and TranSynergy Loewe score prediction models with a 21-34\% reduction in MSE. The impact of utilised data source was found to be more significant and consistent across most synergy models compared to input data fusion architectures. Our findings demonstrated that rapid and less exhaustive in-silico predictions of drug combinations should consider a multiplex of synergy metrics and the combination sensitivity. Moreover, the utilised dataset for model development significantly impacts the subsequent performance of the model.
![image](workflow.png)

# Input Data
-For input data, download the data files from [here](https://drive.google.com/drive/folders/1TmC5PjSCa0-oj551w758kZF2WluP6LK1?usp=sharing) or from IEEE DataPort [here](https://ieee-dataport.org/documents/prediction-anticancer-synergistic-combinations-using-multi-modal-deep-neural-network ) along the models.

-Trained models for early and intermediate fusion architecture across all synergy metrics and CSS implementing either ALmanac or O'neil datasets, together with input data and scripts were deposited in IEEEDataPort with DOI: 10.21227/qqeb-7v80.

Input Files description:

1-Cell lines; List of the 76 cell lines implemented in SynPredict development utilising both Almanac and Oneil datasets.

2-cell_line_Gene_expression_CCLE; Gene expression data for all cell lines in CCLE database.

3-Alvadesc; Physicochemical properties of drugs listed in drugComb v1.3 database (Alvadesc via OCHEM).

4-ECFP: Fingerprints of drugs listed in drugComb v1.3 database.

5-Toxalerts; Toxiciphores identified in the drugs listed in drugComb v1.3 database (Toxalerts via OCHEM).

6-Drugs_Smiles; Canonical smiles and INCHIKeys of the 4087 drugs listed in DrugComb v1.3 database.

7-labels of the target score and pairwise combinations (start with dataset name either Almanac or Oniel and end with score suffix as HSA, Loewe...etc)

# Code implementation

Decompress the downloaded input folder keeping the input folder in the same folder containing the code folder will make the script running smooth.

1- data preparation

Run prepare_data script after amending the input directory to specify the destination of the output data.pkl. Just Amend the input labels_file (line 16 to the dataset and score of interest).

2- Data normalisation

Run normalise_data script utilising the data.pkl file generated from the previous step where the output .h5 sources and target will be generated.


3- Training

Use either Early_fusion_model.py or Intermediate_fusion_training.py for training and nominate the directory for the output model, indices and both predicted and measure scores of the validation.

# Supplementary.pdf

Contains supplementary Table S1- S2 and Figure S1-S2 cited in the [article](https://ieeexplore.ieee.org/document/9609536).

# Citation 

Muhammad Alsherbiny et al "Trustworthy Deep Neural Network for Inferring Anticancer Synergistic Combinations," in IEEE Journal of Biomedical and Health Informatics, doi: 10.1109/JBHI.2021.3126339; https://ieeexplore.ieee.org/document/9609536

Muhammad Alsherbiny, and Ibrahim Radwan June 22, 2021, "Prediction of Anticancer Synergistic Combinations using Multi-Modal Deep Neural Network; SynPredict", IEEE Dataport, doi: https://dx.doi.org/10.21227/qqeb-7v80.




