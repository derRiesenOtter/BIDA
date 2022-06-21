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
    def pairwise_align(self,seq1,seq2):
        resultmatrixzeilen = len(seq1)+1
        resultmatrixspalten = len(seq2)+1
        resultmatrix = np.zeros([resultmatrixzeilen,resultmatrixspalten])
        for i in range(1,resultmatrixzeilen):
           resultmatrix[i][0] = resultmatrix[i-1][0] + self.gap_cost[2]
        for j in range(1,resultmatrixspalten):
           resultmatrix[0][j] = resultmatrix[0][j-1] + self.gap_cost[2]
        for i in range(1,resultmatrixzeilen):
            for j in range(1,resultmatrixspalten):
                match_mismatch = 0
                if seq1[i-1] == seq2[j-1]:
                    match_mismatch = self.gap_cost[0]
                else:
                    match_mismatch = self.gap_cost[1]
                resultmatrix[i][j] = max((resultmatrix[i-1][j-1]+match_mismatch),(resultmatrix[i][j-1]+ self.gap_cost[2]),(resultmatrix[i-1][j]+ self.gap_cost[2]))
        alignedseq1 = ""
        alignedseq2 = ""
        while i != 0 and j != 0:
            backtrack = []
            if (resultmatrix[i-1][j-1])+ self.gap_cost[0] == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i-1][j-1])
            elif (resultmatrix[i-1][j-1])+ self.gap_cost[1] == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i-1][j-1])
            if(resultmatrix[i-1][j])+ self.gap_cost[2] == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i-1][j])
            if(resultmatrix[i][j-1])+ self.gap_cost[2] == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i][j-1])
            maximum = max(backtrack)
            print(maximum)
            if (resultmatrix[i-1][j-1]) == maximum:
                alignedseq1 = seq1[i-1] + alignedseq1
                alignedseq2 = seq2[j-1] + alignedseq2
                i=i-1
                j=j-1
            elif (resultmatrix[i][j-1]) == maximum:
                alignedseq1 = "_" + alignedseq1
                alignedseq2 = seq2[j-1] + alignedseq2
                j=j-1
            elif (resultmatrix[i-1][j]) == maximum:
                alignedseq1 = seq1[i-1] + alignedseq1
                alignedseq2 = "_" + alignedseq2
                i=i-1
        print(resultmatrix)
        print(alignedseq1,alignedseq2, sep = "\n")
        alignedsequences = (alignedseq1,alignedseq2)
        return alignedsequences        
        
seq1 = "AGCGATTCTTG"
seq2 = "TGCCACCTG"

score_matrix = [[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]]

gap_cost = [-2]

align = NeedlemanWunschDnaAligner(0,gap_cost)
align.pairwise_align(seq1,seq2)

def test_pairwise_align():
    #if not "pairwise_align" in globals():
        #print("The function 'pairwise_align' that is to be tested has not been defined yet.")
        #return
    test = NeedlemanWunschDnaAligner(0,[1,-1,-2])
    expected_result = ("AGCGATTCTTG","TGCCAC_CT_G")
    actual_result = test.pairwise_align("AGCGATTCTTG","TGCCACCTG")
    if expected_result == actual_result:
        print("Funktion aligniert Sequenzen korrekt")
    else:
        print("Funktioniert nicht. Erwartetes Ergebnis:",expected_result,"Erhaltenes Ergebnis:",actual_result)
    testi = Aligner
    testi.pairwise_align(0,"AGCGATTCTTG","TGCCACCTG")
    
test_pairwise_align()
