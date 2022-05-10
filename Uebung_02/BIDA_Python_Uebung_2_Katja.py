# Übungsaufgabe 2 aus Bioinformatischer Datenanalyse / Python. Vervollständigen
# Sie bitte dieses Script gemäß der Instruktionen. Führen Sie das script
# mittels der Kommandozeile aus `python3 BIDA_Python_Uebung_2.py`.
#
# TIP:
#-----
# Eine "Exception" (einen Fehler) erzeugt (engl: raise) man mit folgendem Befehl:
# raise Exception("Dimension-Error")

# Einschalten bzw. Ausschalten von z.B. Ausgabe "Matrix ist korrekt"
debug_on = False

def debug(d_print):
    if debug_on:
        print(d_print)
    return

#Matrixmultiplikation
def matrix_mult(m1, m2):
    # Teste, ob Matrizen richtig
    check_matrix(m1)
    check_matrix(m2)
    # Teste, ob Multiplikation möglich
    if not len(m1) == len(m2[0]):
        raise Exception("Dimension-Error")
    # Erstelle eine neue Matrix der gewünschten Größe entsprechend der Ausgangsmatrizen (alle Felder "0")
    m = []
    for a in range (0, len(m1)):
        m.append([0])
        for b in range (1, len(m2[a])):
            m[a].append(0)
    # Multiplikation
    for i in range(0, len(m1)): #Auswahl Reihe in m1
        for j in range (0, len(m2[i])): #Auswahl Spalte in m2
            for k in range (0,len(m2[i])): #Hilfsvariable k um Reihe oder Spalte durchzugehen
                m[j][i] += m1[i][k] * m2[k][j]
    return m

# Prüfe, ob Spalten die gleiche Anzahl an Werten besitzen
def check_matrix(m):
    for i in range(1, len(m)):
        if not len(m[0]) == len(m[i]): # Vergleiche Länge von erster Spalte mit den nächsten Spalten
            raise Exception("Dimension-Error")
    else:
        debug("Matrix ist korrekt")

# normalisiere Matrix
def normalize_matrix(m):
    # Erstelle eine neue Matrix der gewünschten Größe entsprechend der Ausgangsmatrizen (alle Felder "0")
    m_norm = []
    for a in range (0, len(m)):
        m_norm.append([0])
        for b in range (1, len(m[a])):
            m_norm[a].append(0)
    # Normalisierung
    sum_row = 0
    for i in range(0, len(m)): #Auswahl Reihe in Matrix
        for j in range (0, len(m[i])): #Auswahl Spalte in Matrix
            for k in range(0, len(m)):
                sum_row += m[k][i]
            m_norm[i][j] = m[j][i] / sum_row
            sum_row = 0
    return m_norm


# Test the check_matrix function you will implement above:
def test_check_matrix():
    # Check wether the function that is to be tested has been defined yet:
    if not "check_matrix" in globals():
        print("The function 'check_matrix' that is to be tested has not been defined yet")
        # Warum steht hier ein 'return'? Was erspart das im folgenden Teil der
        # Funktion 'test_check_matrix'? A: Wenn die Funktion noch nicht definiert wurde, dann muss kein Test
        # durchgeführt werden, durch return, wird an dieser Stelle unterbrochen
        return

    # ======================================
    # Function has been defined, so test it:
    # ======================================
    m_false_1 = [[1,2], [1,2,3]]
    m_false_2 = [[1,2,3], [4,5]]
    m_correct_1 = [[1,2], [3,4]]
    m_correct_2 = [[1,2,3], [4,5,6], [7,8,9]]
    try:
        # Test one:
        check_matrix(m_false_1)
        # Test two:
        check_matrix(m_false_2)
    except Exception as error:
        if str(error) == "Dimension-Error":
            print("The function 'check_matrix' correctly raises a 'Dimension-Error' if the argument has incorrect dimensions.")
        else:
            print("The function 'check_matrix' does NOT raise a 'Dimension-Error' as expected.")
    # No error expected in the following code ...
    # ... test three:
    check_matrix(m_correct_1)
    # ... test four:
    check_matrix(m_correct_2)

# End of test_check_matrix


# Test the matrix_mult function you will implement above:
def test_matrix_mult():
    # Check wether the function that is to be tested has been defined yet:
    if not "matrix_mult" in globals():
        print("The function 'matrix_mult' that is to be tested has not been defined yet")
        return

    # ======================================
    # Function has been defined, so test it:
    # ======================================

    # Test whether function raises an error if dimensions are not correct:
    m_false = [[1,2], [1,2,3]]
    try:
        matrix_mult(m_false, m_false)
    except Exception as error:
        # Warum schreibt man 'str(error)' in der nächsten Zeile? Stichwort: Datentypen.
        # A: Dem Algorithmus wird durch "str" angegeben, dass es sich bei der Variabel um eine
        # Zeichenkette (String) handelt
        if str(error) == "Dimension-Error":
            print("The function 'matrix_mult' correctly raises a 'Dimension-Error' if the two argument matrices cannot be multiplied.")
        else:
            print("The function 'matrix_mult' does NOT raise a 'Dimension-Error' as expected.")

    # Test matrix multiplication with itself:
    m1_test = [[0.8,0.15,0.05], [0.15,0.8,0.05], [0.05,0.05,0.9]]
    expected_result = [[0.665, 0.2425, 0.09250000000000001], [0.2425, 0.665, 0.09250000000000001], [0.09250000000000001, 0.09250000000000001, 0.8150000000000001]]

    actual_result = matrix_mult(m1_test, m1_test)
    if expected_result != actual_result:
        print("matrix_mult() gave result ", actual_result, ", but expected is ", expected_result)
    else:
        print("matrix_mult() worked as expected")

# End of test_matrix_mult


# Test the normalize_matrix function you will implement above:
def test_normalize_matrix():
    # Check wether the function that is to be tested has been defined yet:
    if not "normalize_matrix" in globals():
        print("The function 'normalize_matrix' that is to be tested has not been defined yet")
        return

    m1_test = [[3,2,1], [2,4,1], [1,1,5]]
    p1 = [[1/2,1/3,1/6], [2/7,4/7,1/7], [1/7,1/7,5/7]]

    actual_result = normalize_matrix(m1_test)
    if p1 != actual_result:
        print("normalize_mult() gave result ", actual_result, ", but expected is ", p1)
    else:
        print("normalize_mult() worked as expected")

# End of test_normalize_matrix


# Check whether a matrix is a probability matrix:
def check_probability_matrix(m):
    for row in m:
        if not len(row) == len(m):
            # Was macht das 'format' in der folgenden Zeile?
            # A: Die Platzhalter {0} und {1} in geschweiften Klammern können durch format bestimmte Variablen
            # oder Werte zugeordnet werden
            print("Matrix 'm' is not quadratic. Found row with {0} cells, but 'm' has {1} rows.".format(len(row), len(m)))
            raise Exception("Dimension-Error")
        if not sum(row) == 1:
            print("Matrix 'm' is not a probability matrix. Found row that sums up to {0}, but expect that it sums to 1.".format(sum(row)))
            raise Exception("Non probability matrix. Row does not sum up to 1.0")

        # Hier fehlt noch ein Test; welcher könnte das sein?
        # A: Test auf Summe == 1 in Spalte

# End of check_probability_matrix


# Execute the above defined tests:
test_check_matrix()
test_matrix_mult()
test_normalize_matrix()

# Matrixmultiplikation der Matrize aus der Vorlesung (M^2, M^3 und M^4)
m_Ami = [[0.8,0.15,0.05], [0.15,0.8,0.05], [0.05,0.05,0.9]]
m_Ami2 = matrix_mult(m_Ami, m_Ami)
m_Ami3 = matrix_mult(m_Ami2, m_Ami)
m_Ami4 = matrix_mult(m_Ami3, m_Ami)

# Ausgabe der Matrizen M, M^2, M^3 und M^4
for l in range(0,len(m_Ami)):
    print(m_Ami[l])
print(" ")
for l in range(0, len(m_Ami)):
    print(m_Ami2[l])
print(" ")
for l in range(0, len(m_Ami)):
    print(m_Ami3[l])
print(" ")
for l in range(0, len(m_Ami)):
    print(m_Ami4[l])
print(" ")