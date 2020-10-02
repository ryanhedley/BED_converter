import pandas as pd
import re

bed_filename = r"ClinGen_haploinsufficiency_gene_GRCh37.bed"

bed_df = pd.read_csv(bed_filename, sep="\t", header=1 )

# print (bed_df)
bed_df_2 = pd.DataFrame (columns=['a','b','c'])

for index, row in bed_df.iterrows():
    
    bed_df_2[index] = 'test'
    print (index, row[1], row[2], row[3], row[4], bed_df_2[1])