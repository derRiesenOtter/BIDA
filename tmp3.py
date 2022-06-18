import numpy as np

seq1 = "AGCGATTCTTG"
seq2 = "TGCCACCTG"

gapcost = [1,-1,-2]

def NeedlemanWunsch(seq1,seq2,gapcost):
    scorematrixzeilen = len(seq1)+1
    scorematrixspalten = len(seq2)+1
    scorematrix = np.zeros([scorematrixzeilen,scorematrixspalten])
    for i in range(1,scorematrixzeilen):
       scorematrix[i][0] = scorematrix[i-1][0] + gapcost[2]
    for j in range(1,scorematrixspalten):
       scorematrix[0][j] = scorematrix[0][j-1] + gapcost[2]
    for i in range(1,scorematrixzeilen):
        for j in range(1,scorematrixspalten):
            match_mismatch = 0
            if seq1[i-1] == seq2[j-1]:
                match_mismatch = gapcost[0]
            else:
                match_mismatch = gapcost[1]
            scorematrix[i][j] = max((scorematrix[i-1][j-1]+match_mismatch),(scorematrix[i][j-1]+gapcost[2]),(scorematrix[i-1][j]+gapcost[2]))
    alignedseq1 = ""
    alignedseq2 = ""
    while i != 0 and j != 0:
        backtrack = []
        if (scorematrix[i-1][j-1])+gapcost[0] == (scorematrix[i][j]):
            backtrack.append(scorematrix[i-1][j-1])
        elif (scorematrix[i-1][j-1])+gapcost[1] == (scorematrix[i][j]):
            backtrack.append(scorematrix[i-1][j-1])
        if(scorematrix[i-1][j])+gapcost[2] == (scorematrix[i][j]):
            backtrack.append(scorematrix[i-1][j])
        if(scorematrix[i][j-1])+gapcost[2] == (scorematrix[i][j]):
            backtrack.append(scorematrix[i][j-1])
        maximum = max(backtrack)
        print(maximum)
        if (scorematrix[i-1][j-1]) == maximum:
            alignedseq1 = seq1[i-1] + alignedseq1
            alignedseq2 = seq2[j-1] + alignedseq2
            i=i-1
            j=j-1
        elif (scorematrix[i][j-1]) == maximum:
            alignedseq1 = "_" + alignedseq1
            alignedseq2 = seq2[j-1] + alignedseq2
            j=j-1
        elif (scorematrix[i-1][j]) == maximum:
            alignedseq1 = seq1[i-1] + alignedseq1
            alignedseq2 = "_" + alignedseq2
            i=i-1
    print(scorematrix)
    print(alignedseq1,alignedseq2, sep = "\n")
    alignedsequences = (alignedseq1,alignedseq2)
    return alignedsequences
    

NeedlemanWunsch(seq1,seq2,gapcost)