import os
import subprocess
from sys import argv


def muscle(input_fasta, output_fasta):
        """
        Run muscle op de command line
        Arguments:
        input_fasta - str - fasta voor msa
        output_fasta - str - naam output met msa
        """
        if os.path.isfile(output_fasta):
                print("MUSCLE is al uitgevoerd")
        else:
                cmd = "muscle -in {} -out {}".format(input_fasta, output_fasta)
                e = subprocess.check_call(cmd, shell=True)

def hmmbuild(hmmbuild_fasta, output_fasta):
        """
        Run hmmbuild op de command line
        Arguments:
        hmmbuild_fasta - str - naam output voor de hmmbuild
        output_fasta - str - fasta voor de hmmbuild
        """
        if os.path.isfile(hmmbuild_fasta):
                print("HMMbuild is al uitgevoerd")
        else:
                cmd = "hmmbuild --amino {} {}".format(hmmbuild_fasta, output_fasta)
                e = subprocess.check_call(cmd, shell=True)

def hmmsearch(hmmsearch_sto, hmmbuild_fasta, database):
        """
        Run hmmsearch op de command line
        Arguments:
        hmmsearch_sto - str - naam output voor de hmmsearch
        hmmbuild_fasta - str - fasta voor de hmmsearch
        database - str - de input voor de database
        """
        if os.path.isfile(hmmsearch_sto):
                print("HMMsearch is al uitgevoerd")
        else:
                cmd = "hmmsearch -A {} {} {}".format(hmmsearch_sto, hmmbuild_fasta, database)
                e = subprocess.check_call(cmd, shell=True)

def main():
        input_fasta = argv[1]
        output_fasta = argv[2]
        print("Input MUSCLE: ", input_fasta)
        print("Output MUSCLE: ", output_fasta)
        muscle(input_fasta, output_fasta)
        output_fasta = argv[2]
        hmmbuild_fasta = argv[3]
        print("Input HMMbuild: ", output_fasta)
        print("Output HMMbuild: ", hmmbuild_fasta)
        hmmbuild(hmmbuild_fasta, output_fasta)
        hmmbuild_fasta = argv[3]
        hmmsearch_sto = argv[4]
        database = argv[5]
        print("Input HMMsearch: ", hmmbuild_fasta)
        print("Output HMMsearch ", hmmsearch_sto)
        print("Database: ", database)
        hmmsearch(hmmsearch_sto, hmmbuild_fasta, database)


main()

