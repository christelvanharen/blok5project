#!/bin/bash

# @brief 
# Loops together with pipeline.py script iterates three times to find orthologues using locally downloaded uniprot db, aligns these and creates HMM's
# Requires several files:
# pipeline.py
# uniprot_sprot.fasta



echo "Type the name of the file you want to iterate. Input is BLAST fasta output."
inputfile="USER INPUT"
read -p "Enter input file: " inputfile


# For three loops, number is a variable
for number in {1..3}
do 

# For first iteration, rename first file to have a number
if [ "$number" -eq "1" ] ; then
    mv $inputfile researchfileloop$number.fasta
    
# For other loops, take hmmsearch file of previous loop, change the name for next loop
    else
    previousnum=$((number-1))
    mv hmmsearchloop$previousnum.fasta researchfileloop$number.fasta
    fi

# Calling python program for file processing
python3 pipeline.py researchfileloop$number.fasta muscleloop$number.fasta hmmbuildloop$number hmmsearchloop$number uniprot_sprot.fasta $number

# Change format from .sto to .fasta
esl-reformat -o hmmsearchloop$number.fasta fasta hmmsearchloop$number

# Print in terminal current running iteration
echo "Iteration no: $number"

done

# Align final iteration and produce hmm profile

muscle -in researchfileloop3.fasta -out muscle4.fasta
hmmbuild --amino hmmbuild_final_product muscle4.fasta


