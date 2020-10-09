import os
import subprocess
from sys import argv

def muscle(input_fasta, output_muscle):
        """
        De MUSCLE tool wordt hier gerund met behulp van iteraties.sh
        Args:
                input_fasta: een FASTA bestand met sequenties
                output_muscle: een MSA

        Returns: output_muscle
        """
        if os.path.isfile(output_muscle):
                print("MUSCLE is al uitgevoerd")
        else:
                cmd = "muscle -in {} -out {}".format(input_fasta,
                                                     output_muscle)
                e = subprocess.check_call(cmd, shell=True)

def hmmbuild(hmmbuild_fasta, output_muscle):
        """
        De HMMbuild wordt gerund met de output_muscle file
        Args:
                hmmbuild_fasta: de output van deze functie
                output_muscle: de MSA uit MUSCLE

        Returns: hmmbuild_fasta
        """
        if os.path.isfile(hmmbuild_fasta):
                print("HMMbuild is al uitgevoerd")
        else:
                cmd = "hmmbuild --amino {} {}".format(hmmbuild_fasta,
                                                      output_muscle)
                e = subprocess.check_call(cmd, shell=True)

def hmmsearch(hmmsearch_sto, hmmbuild_fasta, database):
        """
        De HMMsearch wordt gerund met de hmmbuild_fasta file
        Args:
                hmmsearch_sto: de output file in STOCKHOLM format
                hmmbuild_fasta: de input file, afkomstig van HMMbuild
                database: de database die gebruikt wordt

        Returns: hmmsearch_sto
        """
        if os.path.isfile(hmmsearch_sto):
                print("HMMsearch is al uitgevoerd")
        else:
                cmd = "hmmsearch -A {} {} {}".format(hmmsearch_sto, hmmbuild_fasta, database)
                e = subprocess.check_call(cmd, shell=True)

def main():
        input_fasta = argv[1]
        output_muscle = argv[2]
        print("Input MUSCLE: ", input_fasta)
        print("Output MUSCLE: ", output_muscle)
        muscle(input_fasta, output_muscle)
        output_muscle = argv[2]
        hmmbuild_fasta = argv[3]
        print("Input HMMbuild: ", output_muscle)
        print("Output HMMbuild: ", hmmbuild_fasta)
        hmmbuild(hmmbuild_fasta, output_muscle)
        hmmbuild_fasta = argv[3]
        hmmsearch_sto = argv[4]
        database = argv[5]
        print("Input HMMsearch: ", hmmbuild_fasta)
        print("Output HMMsearch ", hmmsearch_sto)
        print("Database: ", database)
        hmmsearch(hmmsearch_sto, hmmbuild_fasta, database)


main()

