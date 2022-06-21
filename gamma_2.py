import numpy as np
import pandas as pd

# it's free real estate ;)

# score_matrix muss als pandas (ggf. noch nicht installiert) datatable vorliegen (siehe Testfunktion) (macht das arbeiten damit einfacher)

# Klassen wie in Vorlsesung / Aufgabenstellung beschrieben angelegt

class Aligner:
    def __init__(self,score_matrix, gap_cost):
        self.score_matrix = score_matrix
        self.gap_cost = gap_cost

    def pairwise_align(self,seq1,seq2):
        raise NotImplementedError ("This is an abstract class, which can not align", seq1,"and",seq2)

class NeedlemanWunschDnaAligner(Aligner):
    def pairwise_align(self,seq1,seq2):
        # Erstellen einer Matrix mit den richtigen Maßen (+1 für die Gap Felder)
        resultmatrixzeilen = len(seq1)+1
        resultmatrixspalten = len(seq2)+1
        resultmatrix = np.zeros([resultmatrixzeilen,resultmatrixspalten])
        # Initialisierung der ersten (Gap-)Zeile und (Gap-)Spalte
        for i in range(1,resultmatrixzeilen):
           resultmatrix[i][0] = resultmatrix[i-1][0] + self.gap_cost
        for j in range(1,resultmatrixspalten):
           resultmatrix[0][j] = resultmatrix[0][j-1] + self.gap_cost
        # Die folgenden beiden for-Schleifen durchlaufen die komplette Matrix
        for i in range(1,resultmatrixzeilen):
            for j in range(1,resultmatrixspalten):
                # und tragen den maximalen Wert aus Match/Mismatch diagonal, gap von links und gap von oben in das entsprechende Feld der Resultmatrix
                resultmatrix[i][j] = max((resultmatrix[i-1][j-1]+self.score_matrix[seq1[i-1]][seq2[j-1]]),(resultmatrix[i][j-1]+ self.gap_cost),(resultmatrix[i-1][j]+ self.gap_cost))
        # Die Resultmatrix ist nun fertig
        # Als nächstes durchlaufen wir die Matrix von hinten, um die Sequenzen auszulesen
        # Dafür legen wir die beiden folgenden Variablen mit leerem String an
        alignedseq1 = ""
        alignedseq2 = ""
        # i und j stehen noch auf dem Wert für das Feld links unten, und die Schleife soll aufhären, wenn wir wieder am Anfang sind
        while i != 0 and j != 0:
            # Jetzt müssen wir alle möglichen Vorgänger betrachten und schauen ob es möglich war von diesem auf das betrachtete Feld zu kommen
            # dazu legen wir uns eine leere Liste an
            backtrack = []
            # in diese schreiben wir für ein Feld dann immer alle möglichen Vorgänger
            # Wir haben einen möglichen Vorgänger, wenn das Vorgängerfeld + Gapcost/ Wert aus Scorematrix gleich dem betrachtetem Feld ist
            if (resultmatrix[i-1][j-1])+ self.score_matrix[seq1[i-1]][seq2[j-1]] == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i-1][j-1])
            if(resultmatrix[i-1][j])+ self.gap_cost == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i-1][j])
            if(resultmatrix[i][j-1])+ self.gap_cost == (resultmatrix[i][j]):
                backtrack.append(resultmatrix[i][j-1])
            # von den möglichen Vorgängern wollen wir jetzt den günstigsten Wert wählen. Das machen wir über die max funktion.
            maximum = max(backtrack)
            # Nachdem wir unseren Wert gefunden haben müssen wir noch unsere Variablen mit den leeren Strings mit Buchstaben und gaps füllen
            # mit den folgenden befehlen prüfen wir welcher Vorgänger der maximale war und schreiben ihn, oder ein gap in unseren String (vorne dran, da wir ja rückwärts durchlaufen)
            if (resultmatrix[i-1][j-1]) == maximum:
                alignedseq1 = seq1[i-1] + alignedseq1
                alignedseq2 = seq2[j-1] + alignedseq2
                # weiter müssen wir natürlich auch unser i und j entsprechend anpassen
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
        # Zum Ende wollen wir noch der Aufgabenstellung entsprechen und schreiben die beiden Sequenzen in eine Liste, die wir dann zurückgeben
        alignedsequences = (alignedseq1,alignedseq2)
        return alignedsequences        

# Nachfolgend der Test, ob richtig aligned wird und ein notimplementederror aausgegeben wird

def test_pairwise_align():
    # Wie anfangs bereits erwähnt wollen wir die Scorematrix als pandas datatable übergeben - Grund dafür war, dass man ein Feld im Datatable mit eingabe der Buchstaben der Sequenz ausgeben kann
    # Umwandeln der Matrix in datatable
    score_matrix = pd.DataFrame([[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]])
    # Benamen der Spalten und Zeilen mit den Buchstaben
    score_matrix.columns = ["A","G","C","T"]
    score_matrix.index = ["A","G","C","T"]
    gap_cost = -2
    # test wird als Objekt der Klasse Needle... definiert und erhält direkt die scorematrix und die gap costs
    test = NeedlemanWunschDnaAligner(score_matrix,gap_cost)
    # unser erwartetes Ergebnis...
    expected_result = ("AGCGATTCTTG","TGCCAC_CT_G")
    # unser erhaltenes Ergebnis, durch aufruf der funktion pairwise_align über unser test Objekt
    actual_result = test.pairwise_align("AGCGATTCTTG","TGCCACCTG")
    # Alignment geklappt? Entsprechende Ausgabe
    if expected_result == actual_result:
        print("Funktion aligniert Sequenzen korrekt zu AGCGATTCTTG und TGCCAC_CT_G")
    else:
        print("Funktioniert nicht. Erwartetes Ergebnis:",expected_result,"Erhaltenes Ergebnis:",actual_result)
    # Wir erstellen ein zweites Testobjekt, aber von der Klasse Aligner
    testi = Aligner(score_matrix,gap_cost)
    # Dieses wird nun, wenn man auf die Funktion pairwise_alignment zugreifen möchte, den NotImplementedError ausgeben, wenn nicht gibt es die entsprechende Meldung
    try:
        testi.pairwise_align("AGCGATTCTTG","TGCCACCTG")
    except NotImplementedError:
        print('Funktion erhebt den NotImplementedError wie erwartet')
    else:
        print('Funktion erhebt den NotImplementedError nicht wie erwartet')

# Dann können wir das ganze laufen lassen

test_pairwise_align()
