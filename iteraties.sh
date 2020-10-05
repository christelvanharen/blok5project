for number in 1 2 3
do python3 pipeline.py thioredoxine_swissprot.fasta muscle_swissprot.fasta hmmbuild_swissprot_muscle hmmsearch_swissprot uniprot_sprot.fasta
do python3 pipeline.py thioredoxine_pdb.fasta muscle_pdb.fasta hmmbuild_pdb_muscle hmmsearch_pdb pdb_seqres.fasta




