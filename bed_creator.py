import pandas as pd
from tkinter.filedialog import askopenfilename


#Download BED file from ftp://ftp.clinicalgenome.org/

#Import BED file using Tkinter file dialogue
def openfile():
    bed_filename = askopenfilename(title = "Select file", filetypes = (("BED files","*.bed"),("All Files","*.*")))
    return (bed_filename)



#Convert imported BED file to Pandas DataFrame
def convert_bed_to_df(bed_filename):
    #columns = ['chr', 'start', 'stop', 'gene', 'dosage']
    bed_df = pd.read_csv(bed_filename, sep="\t", header=1 )
    print("Reading... ",bed_filename)

    return(bed_df)


#Convert Pandas Dataframe to BED file in required format (with RGB colours)
def convert_df_to_bed(bed_filename, bed_df):
    bed_filename = bed_filename + '_converted.bed'

    # RGB Colours
    score_0 = "0,255,0"     #Green
    score_1 = "255,255,0"   #Yellow
    score_2 = "255,125,0"   #Orange
    score_3 = "255,0,0"     #Red
    score_30 = "0,255,255"  #Cyan
    score_40 = "0,255,0"    #Green

    # Add BED file header
    header_row = "track name='ClinGen Gene Curation Haploinsufficiency Scores' db=hg19 itemRgb='On' \n"

    # Create new BED file with changes
    with open(bed_filename, "w") as f:
        f.writelines(header_row)

        for index, row in bed_df.iterrows():
            dosage_score = int(row[4])

            # Determine the colour from the dosage score
            if dosage_score == 0:
                dosage_colour = score_0
            if dosage_score == 1:
                dosage_colour = score_1
            if dosage_score == 2:
                dosage_colour = score_2
            if dosage_score == 3:
                dosage_colour = score_3
            if dosage_score == 30:
                dosage_colour = score_30
            if dosage_score == 40:
                dosage_colour = score_40

            
            # Create each line to add to new BED file
            line = (
                str(row[0]) + "\t" +        #chr
                str(row[1]) + "\t" +        #start
                str(row[2]) + "\t" +        #stop
                str(row[3]) + "\t" +        #gene
                str(row[4]) + "\t" +        #score
                "." +  "\t" +               #dot
                str(row[1]) + "\t" +        #start
                str(row[2]) + "\t" +        #stop
                str(dosage_colour) + "\n"   #RGB colour
            )

            f.writelines(line)

    print("Writing... ",bed_filename)



def main():
    bed_filename = openfile()
    bed_df = convert_bed_to_df(bed_filename)
    convert_df_to_bed(bed_filename, bed_df)


if __name__ == "__main__":
    main()

