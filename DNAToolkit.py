# DNA Toolkit file
import collections

Nucleotides = ["A", "C", "G", "T"]

# Check a given sequence to validate it is a DNA SyntaxWarning
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

# Count Nucleotide frequency
def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
#    return dict(collections.Counter(seq))
