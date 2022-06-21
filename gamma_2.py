import numpy as np
import pandas as pd

class Aligner:
    def __init__(self,score_matrix, gap_cost):
        self.score_matrix = score_matrix
        self.gap_cost = gap_cost

    def pairwise_align(self,seq1,seq2):
        raise NotImplementedError ("This is an abstract class, which can not align", seq1,"and",seq2)

class NeedlemanWunschDnaAligner(Aligner):
    def pairwise_align(self,seq1,seq2):
        resultmatrixzeilen = len(seq1)+1
        resultmatrixspalten = len(seq2)+1
        resultmatrix = np.zeros([resultmatrixzeilen,resultmatrixspalten])
        for i in range(1,resultmatrixzeilen):
           resultmatrix[i][0] = resultmatrix[i-1][0] + self.gap_cost
        for j in range(1,resultmatrixspalten):
           resultmatrix[0][j] = resultmatrix[0][j-1] + self.gap_cost
        for i in range(1,resultmatrixzeilen):
            for j in range(1,resultmatrixspalten):
                resultmatrix[i][j] = max((resultmatrix[i-1][j-1]+self.score_matrix[seq1[i-1]][seq2[j-1]]),(resultmatrix[i][j-1]+ self.gap_cost),(resultmatrix[i-1][j]+ self.gap_cost))
        alignedseq1 = ""
        alignedseq2 = ""
        while i != 0 and j != 0:
            backtrack = []
            if (resultmatrix[i-1][j-1])+ self.score_matrix[seq1[i-1]][seq2[j-1]] == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i-1][j-1])
            if(resultmatrix[i-1][j])+ self.gap_cost == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i-1][j])
            if(resultmatrix[i][j-1])+ self.gap_cost == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i][j-1])
            maximum = max(backtrack)
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
        alignedsequences = (alignedseq1,alignedseq2)
        return alignedsequences        

def test_pairwise_align():
    score_matrix = pd.DataFrame([[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]])
    score_matrix.columns = ["A","G","C","T"]
    score_matrix.index = ["A","G","C","T"]
    gap_cost = -2
    test = NeedlemanWunschDnaAligner(score_matrix,gap_cost)
    expected_result = ("AGCGATTCTTG","TGCCAC_CT_G")
    actual_result = test.pairwise_align("AGCGATTCTTG","TGCCACCTG")
    if expected_result == actual_result:
        print("Funktion aligniert Sequenzen korrekt zu AGCGATTCTTG und TGCCAC_CT_G")
    else:
        print("Funktioniert nicht. Erwartetes Ergebnis:",expected_result,"Erhaltenes Ergebnis:",actual_result)
    testi = Aligner
    try:
        testi.pairwise_align(score_matrix,"AGCGATTCTTG","TGCCACCTG")
    except NotImplementedError:
        print('Funktion erhebt den NotImplementedError wie erwartet')
    else:
        print('Funktion erhebt den NotImplementedError nicht wie erwartet')
    
test_pairwise_align()
