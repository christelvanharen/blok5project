#!/bin/bash
for number in {1..3}
do 

if [ "$number" -eq "1" ] ; then
    mv thioredoxine_swissprot.fasta thioredoxine_swissprot$number.fasta
    
    else
    previousnum = $number-1
    esl-reformat -o hmmsearch_swissprot$number.fasta hmmsearch_swissprot$number.sto
    mv hmmsearch_swissprot$previousnum.fasta thioredoxine_swissprot$number.fasta
    fi

python3 pipeline.py thioredoxine_swissprot$number.fasta muscle_swissprot$number.fasta hmmbuild_swissprot_muscle$number hmmsearch_swissprot$number.sto uniprot_sprot.fasta $number


echo "Number: $number"

done

# do 
# muscle -in thioredoxine_swissprot.fasta -out muscle_swissprot.fasta
# hmmbuild --amino muscle_swissprot.fasta final_product

# done
