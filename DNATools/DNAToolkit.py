# DNA Toolkit file
import collections
from sequences import *

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

# Transcription (we love uracil)
def transcription(seq):
    """Replaces Thymine with Uracil"""
    return seq.replace("T", "U")

# reverse complement
def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

# GC content
def gc_content(seq):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

# GC subset content of a sub sequence length of k
def gc_content_subset(seq, k=20):
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subset = seq[i:i + k]
        res.append(gc_content(subset))
    return res
