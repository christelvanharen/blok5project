for number in 1 2 3 4
do
python3 pipeline.py thioredoxine_swissprot.fasta muscle_swissprot.fasta hmmbuil>
echo "Number: $number"
if [number -eq 4] ; then
break
done
do
muscle -in thioredoxine_swissprot.fasta -out muscle_swissprot.fasta
hmmbuild --amino muscle_swissprot.fasta final_product
echo "idioot"
done
