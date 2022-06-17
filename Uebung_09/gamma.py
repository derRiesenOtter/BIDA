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