#Aufgabe 1a)
# *args und **kwargs in die Klammer
from functools import reduce


a = "Affe"
b = "Banane"
c = "Ape"
d = "Monkey"

def print_unnamed_arguments(*args):
    for arg in args: 
        print(arg, end=" ")
    print("")        

print_unnamed_arguments(a,b,c,d)

#Aufgabe 1b)

def print_named_arguments(a, b):
    print(a,b)

print_named_arguments(a="monkey",b="ape")        

#Aufgabe 1c)

def print_some_named_arguments(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value)) # was passiert hier?

print_some_named_arguments(name="Mooooonkey", surname="Ape")        

#Aufgabe 1d)

def print_named_arguments_standardvalue(a, b, reverse=False):
    if not reverse: 
        print(a,b)
    else:
        print(b,a)

print_named_arguments_standardvalue(a,b, reverse=True)  

#Aufgabe 1e)

def print_everything(*args,reverse = False, **kwargs):
    if not reverse:
        print(args)
        for key, value in kwargs.items():
            print(key, value, sep=": ")
    else:
        for key, value in kwargs.items():
            print(key, value, sep=": ")
        print(args)

print_everything(a,b,c,d,reverse = False,e = "Orang Utang", f = "Bonobo")

#Aufgabe 2 

def my_sum(*numbers):
    sum = 0
    for number in numbers: 
        sum += number
    return sum

def test_my_sum():
    if not "my_sum" in globals():
        print("Funktion nicht gefunden")
    else:
        a = 1
        b = 2
        c = 3
        d = 4
        expected_result_a_to_b = 3
        expected_result_a_to_d = 10
        actual_result_a_to_b = my_sum(a,b)
        actual_result_a_to_d = my_sum(a,b,c,d)
        if(expected_result_a_to_b == actual_result_a_to_b)and(expected_result_a_to_d == actual_result_a_to_d):
            print("Funktion my_sum funktioniert")
        else:
            print("Funktion enthält Fehler. Erwartet Ergebnisse:",expected_result_a_to_b,expected_result_a_to_d,"Erhaltene Ergebnisse:", actual_result_a_to_b, actual_result_a_to_d)

test_my_sum()

#Aufgabge 3

def report_named_args(**kwargs):
    print(kwargs)

report_named_args(a="wololo", b="wululu")

#Aufgabe 4

def report_named_args_mod(report_sep=": ", **kwargs):
    for key, value in kwargs.items():
        print(key, value, sep=report_sep)

report_named_args_mod(report_sep= "_", a="wololo", b="wululu")

#Aufgabe 5

def sum_or_mult(*numbers, mult=False):
    if not mult:
        sum = 0
        for number in numbers:
            sum += number
        return sum
    else:
        product = 1
        for number in numbers:
            product *= number
        return product

def test_sum_or_mult():
    if not "sum_or_mult" in globals():
        print("Funktion sum_or_mult nicht gefunden")
    else:
        a=2
        b=3
        c=4
        expected_result_a_and_b = 5
        expected_result_a_times_b_times_c = 24
        actual_result_a_and_b = sum_or_mult(a,b)
        actual_result_a_times_b_times_c = sum_or_mult(a,b,c,mult=True)
        if (expected_result_a_and_b == actual_result_a_and_b)and(expected_result_a_times_b_times_c==actual_result_a_times_b_times_c):
            print("Funktion funktioniert")
        else:
            print("Funktion enthält Fehler: Erwartete Ergebnisse:", expected_result_a_and_b, expected_result_a_times_b_times_c,"Erhaltene Ergebnisse:", actual_result_a_and_b, actual_result_a_times_b_times_c)

test_sum_or_mult()

#Aufgabe 6a) und 6b) 

#definition in python siehe folgende... Übergabe ist in print zu sehen

f = lambda x,y : x+y
print(f(1,1))

#Aufgabe 6c)

#map akzeptiert eine Funktion und eine Sequenz (oder mehrere, siehe zweites Beispiel) und gibt die ergebnisse der funktion auf alle elemente der liste wieder - man spart sich die Definition der Funktion...

C = [39.2, 36.5, 37.3, 38, 37.8] 
F = list(map(lambda x: 9/5*x + 32, C))
print(F)

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
print(list(map(lambda x, y, z : x+y+z, a, b, c)))

#reduce führt rechenoperation mit einer liste aus und reduziert sie damit auf ein ergebnis

print(reduce(lambda x, y: x + y,a))

#filter (nicht in Aufgabe gefragt, aber m.E.n. vielleicht mal nützlich), gibt Liste aus mit nur noch den Elementen, die eine Bedingung erfüllen...

final_list = list(filter(lambda x: (x%2 == 0) , a))
print(final_list)

#Aufgabe 6d)

print(list(map(lambda x: x*x,range(-10,10+1))))
print(list(map(lambda x: x*x*x,range(-10,10+1))))

#Aufgabe 6e)

print(reduce(lambda x,y: x+y,range(-10,10+1)))

#Aufgabe 6f)

start_number=100
print(reduce(lambda x,y: x+y, range(1,3+1), start_number))

#Aufgabe 7a)

me = {"name": "Robin", "surname": "Ender", "age": "23", "cleans_laptop_in_dishwasher": True}

#Aufgabe 7b)

report_named_args_mod(me=me)

#Aufgabe 7c)
sonic = {"name":"sonic", "surname": "the hedgehog", "age": "hmm","sport": "running"}
me = {"name": "Robin", "surname": "Ender", "age": "23", "cleans_laptop_in_dishwasher": True, "most_liked_athlete":sonic}

