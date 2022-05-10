#Aufgabe 1
print ("Bitte geben Sie Ihren Namen ein: ", end="")
print ("und zwar in dieser Zeile")

#Aufgabe 2
print ("name\tvorname\talter\twohnort")

#Aufgabe 3
#siehe extra Datei mit Endung lese_eingabe

#Aufgabe 4
#python -m pip install termcolor im terminal eingeben

#Aufgabe 4 die zweite
def größtergemeinsamerTeiler(a,b):
    if a >= b:
        größereZahl = a
        kleinereZahl = b
    else:
        größereZahl = b
        kleinereZahl = a
    Rest = kleinereZahl
    while größereZahl % kleinereZahl != 0:
        Rest = größereZahl % kleinereZahl
        größereZahl = kleinereZahl
        kleinereZahl = Rest
    return(Rest)


def test_größtergemeinsamerTeiler():
    if not "größtergemeinsamerTeiler" in globals():
        print("Funktion nicht gefunden")
    else:
        a = 544
        b = 391
        expected_result = 17
        actual_result = größtergemeinsamerTeiler(a,b)
        if expected_result == actual_result:
            print("Funktion findet den größten gemeinsamen Teiler")   
        else:
            print("Funktion enthält einen Fehler, erwartetes Ergebnis:",expected_result,"erhaltenes Ergebnis:",actual_result) 
    
test_größtergemeinsamerTeiler()   

#Aufgabe 5

def Fakultät(a):
    Fakultät
    Faku = 1
    for i in range (1, a+1):
        Faku = Faku * i
    return(Faku)


def test_Fakultät():
    if not "Fakultät" in globals():
        print("Funktion nicht gefunden")
    else:
        a = 5
        expected_result = 120
        actual_result = Fakultät(a)
        if expected_result == actual_result:
            print("Funktion berechnet Fakultät korrekt")   
        else:
            print("Funktion enthält einen Fehler, erwartetes Ergebnis:",expected_result,"erhaltenes Ergebnis:",actual_result)

test_Fakultät()

#Aufgabe 6-8 in Datei plots