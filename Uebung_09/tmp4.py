import numpy as np

seq1 = "AGCGATTCTTG"
seq2 = "TGCCACCTG"

gapcost = [1,-1,-2]

def NeedlemanWunsch(seq1,seq2,gapcost):
    score_matrixzeilen = len(seq1)+1
    score_matrixspalten = len(seq2)+1
    score_matrix = np.zeros([score_matrixzeilen,score_matrixspalten])
    for i in range(1,score_matrixzeilen):
       score_matrix[i][0] = score_matrix[i-1][0] + gapcost[2]
    for j in range(1,score_matrixspalten):
       score_matrix[0][j] = score_matrix[0][j-1] + gapcost[2]
    for i in range(1,score_matrixzeilen):
        for j in range(1,score_matrixspalten):
            match_mismatch = 0
            if seq1[i-1] == seq2[j-1]:
                match_mismatch = gapcost[0]
            else:
                match_mismatch = gapcost[1]
            score_matrix[i][j] = max((score_matrix[i-1][j-1]+match_mismatch),(score_matrix[i][j-1]+gapcost[2]),(score_matrix[i-1][j]+gapcost[2]))
    alignedseq1 = ""
    alignedseq2 = ""
    backtrack_stack = []
    while i != 0 and j != 0:
        backtrack = []
        if (score_matrix[i-1][j-1])+gapcost[0] == (score_matrix[i][j]):
            backtrack.append(score_matrix[i-1][j-1])
        elif (score_matrix[i-1][j-1])+gapcost[1] == (score_matrix[i][j]):
            backtrack.append(score_matrix[i-1][j-1])
        if(score_matrix[i-1][j])+gapcost[2] == (score_matrix[i][j]):
            backtrack.append(score_matrix[i-1][j])
        if(score_matrix[i][j-1])+gapcost[2] == (score_matrix[i][j]):
            backtrack.append(score_matrix[i][j-1])
        if len(backtrack) == 1: 
            maximum = backtrack[0]
        else:

            maximum = max(backtrack_stack.pop())
        print(maximum)
        if (score_matrix[i-1][j-1]) == maximum:
            alignedseq1 = seq1[i-1] + alignedseq1
            alignedseq2 = seq2[j-1] + alignedseq2
            i=i-1
            j=j-1
        elif (score_matrix[i][j-1]) == maximum:
            alignedseq1 = "_" + alignedseq1
            alignedseq2 = seq2[j-1] + alignedseq2
            j=j-1
        elif (score_matrix[i-1][j]) == maximum:
            alignedseq1 = seq1[i-1] + alignedseq1
            alignedseq2 = "_" + alignedseq2
            i=i-1
    print(score_matrix)
    print(alignedseq1,alignedseq2, sep = "\n")
    alignedsequences = (alignedseq1,alignedseq2)
    return alignedsequences
    

NeedlemanWunsch(seq1,seq2,gapcost)