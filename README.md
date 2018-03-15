## History of bladder cancer in Minnesota 1988-2013 & Visualization of FAT3 gene and amino acids

*Author: Minh Huyen Nguyen*

*CS 111 - Spring 2017* 

*Denison University*

### Bladder Cancer in Human 

Bladder cancer is one of the most common urinary system malignancies that leads to cause of cancer related death of men over the world. There are several types of cancer arising from the bladder involving epithelial lining of urinary bladder such as carcinoma, non-epithelial cancers such as lymphoma or sarcoma. Bladder cancer are predicted to occur at any age both in male and female, but the incidence is three to four times greater in male than in female.

Cadherins belong to a class of calcium-dependent transmembrane proteins which play important roles in cell adhesion, cell aggregation and cell sorting within tissues. Cadherins are important in both prokaryotes and eukaryotes. The third Fat Cadherin gene in human, FAT3, was found on chromosome 11q14.3 consisting of 26 exons and encoding 4557 amino acids. According to the Cancer Browser Database from the University of California-Santa Cruz, FAT3 is reported to be mutated in 10% of bladder carcinomas. There is a 1.63-fold decrease in FAT3 gene expressions in bladder tumor samples compared to those in normal tissue samples (p=0.00037) (The UCSC). 

### Methods

- 1st part will take a look into the data sets of clinical studies  retrieved from http://www.cbioportal.org. 
  - Two histograms will be created in comparing the overall survival status by genders and cancer’s stages. Two sample t-test and paired t-test will be conducted in order to testing the significance in differences between independent groups. A scatter plot and a linear regression will plot the relationship between the total number of lymph nodes removed and the overall survival in months since initial diagnosis of patients. 
  
- 2nd part will focus on reading a text file containing 5000 first base pairs of DNA sequence of FAT3 gene. 
  - Gene sequence is retrieved from www.ncbi.nlm.nih.gov/gene. This sequence will be drawn into bars with intervals of alternating colors over the sequence to indicate the locations of open reading frames. The sequence will be then translated into amino acid sequence. The translation will use the codon table which is made into dictionary in a separated (Python) file. Similar to the finding opening reading frames in DNA strands, this amino acid sequence will be drawn in bars with intervals of four different color which denote four different types of amino acid (neutral non-polar, neutral polar, acidic polar and basic polar).

### Required packages & installation

```
readr
dplyr
ggplot2
nympy
turtle
matplotlib
```

### References

Gao, J., et al. “Integrative Analysis of Complex Cancer Genomics and Clinical Profiles Using the CBioPortal.” Science Signaling, vol. 6, no. 269, 2013, doi:10.1126/scisignal.2004088.

Gene FAT3. Bethesda (MD): National Library of Medicine (US), National Center for Biotechnology Information. Available from: https://www.ncbi.nlm.nih.gov/gene/

Ethan, C. et al. “The CBio Cancer Genomics Portal: An Open Platform for Exploring Multidimensional Cancer Genomics Data.” Cancer Discovery, vol. 2, no. 10, 2012, pp. 960–960., doi:10.1158/2159-8290.cd-12-0326.

Minnesota Public Health Data Access. Minnesota Department of Health. Available from: https://apps.health.state.mn.us/mndata/

Parts of the project based on "Discovering Computer Science: Interdisciplinary Problems, Principles, and Python Programming" 
by Dr. Jessen Havill (Professor, Department of Computer Science & Mathematics - Denison University)
