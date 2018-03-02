## History of bladder cancer in Minnesota & Visualization of FAT3 gene and amino acids

*Author: Minh Huyen Nguyen*
*CS 111 - Spring 2017* 
*Denison University*

**Introduction of Bladder cancer in Human**

Bladder cancer is one of the most common urinary system malignancies that leads to cause of cancer related death of men over the world. There are several types of cancer arising from the bladder involving epithelial lining of urinary bladder such as carcinoma, non-epithelial cancers such as lymphoma or sarcoma. Bladder cancer are predicted to occur at any age both in male and female, but the incidence is three to four times greater in male than in female.

Cadherins belong to a class of calcium-dependent transmembrane proteins which play important roles in cell adhesion, cell aggregation and cell sorting within tissues. Cadherins are important in both prokaryotes and eukaryotes. The third Fat Cadherin gene in human, FAT3, was found on chromosome 11q14.3 consisting of 26 exons and encoding 4557 amino acids. According to the Cancer Browser Database from the University of California-Santa Cruz, FAT3 is reported to be mutated in 10% of bladder carcinomas. There is a 1.63-fold decrease in FAT3 gene expressions in bladder tumor samples compared to those in normal tissue samples (p=0.00037) (The UCSC). 

**Methods**

This project will include two main parts. The first part will take a look into the data sets retrieved from http://www.cbioportal.org (data_bcr_clinal_data_patient.csv). Two histograms will be created in comparing the overall survival status by genders and cancer’s stages. Two sample t-test and paired t-test will be conducted in order to testing the significance in differences between independent groups. A scatter plot and a linear regression will plot the relationship between the total number of lymph nodes removed and the overall survival in months since initial diagnosis of patients. The second part will focus on reading a text file containing 5000 first base pairs of DNA sequence of FAT3 gene. Gene sequence is retrieved from www.ncbi.nlm.nih.gov/gene. This sequence will be drawn into bars with intervals of alternating colors over the sequence to indicate the locations of open reading frames. The sequence will be then translated into amino acid sequence. The translation will use the codon table which is made into dictionary in a separated (Python) file. Similar to the finding opening reading frames in DNA strands, this amino acid sequence will be drawn in bars with intervals of four different color which denote four different types of amino acid (neutral non-polar, neutral polar, acidic polar and basic polar).

•	Some Python concepts needed in this project:
-	Reading csv file; working with strings, floats, indices; conditional statements, loops, 
-	Plotting histograms, scatter plots, linear regression
-	Creating lists, tuples, dictionary
-	Drawing using turtle 
