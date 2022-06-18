import numpy as np

class Aligner:
    def __init__(self,score_matrix, gap_cost):
        self.score_matrix = score_matrix
        self.gap_cost = gap_cost

    def pairwise_align(self,seq1,seq2):
        raise NotImplementedError(
            "This is an abstract class, which can not align",
            seq1,"and",seq2) 

class NeedlemanWunschDnaAligner(Aligner):
    def pairwise_align(self,seq1,seq2,gapcost):
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
        


#s1 = Aligner("ABC","DEF")
#s2 = Aligner("ABC","DEF")
#seq1= "ABC"
#seq2 = "DEF"
#s1.pairwise_align(seq1,seq2)




#def NeedlemanWunsch(u,v,δ):
    #S[0][0] = 0
    #for i in range(1,len(u)+2):
       # S[i][0] = S[i−1][0] #+ δ(ui , −)
    #for j in range(1,len(v)+2):
    #    S[0][j] = S[0][j−1] #+ δ(−, vj )
   # for i in range(1,len(u)+2):
   #     for j in range(1,len(v)+2):
    #        S[i][j] = max()

# Kostenfaktor noch implementieren

#Print(max(7,5,9))