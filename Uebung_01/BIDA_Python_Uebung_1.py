# 7a)
print("Aufgabe 7a")
print(13 - 5 * 2 + 12 / 6)
# 7b)
# mod entspricht %
print("Aufgabe 7b")
print(6 + (27 % 5) * 3)
# 7c)
print("Aufgabe 7c")
print(1 / 2 - 1 / 4 + (4 + 3 / 8) * 2)

# 8)
print("Aufgabe 8")
def calc_1():
    return(13 - 5 * 2 + 12 / 6)
def calc_2():
    return(6 + (27 % 5) * 3)
def calc_3():
    return(1 / 2 - 1 / 4 + (4 + 3 / 8) * 2)

def test_calc_1():
    # Check wether the function that is to be tested has been defined yet:
    if not "calc_1" in globals():
        print("The function 'calc_1' that is to be tested has not been defined yet")
    else:
        # Function has been defined, so test it:
        expected_result = 5
        actual_result = calc_1()
        if expected_result != actual_result:
            print("calc_1() gave result ", actual_result, ", but expected is ", expected_result)
        else:
            print("calc_1() worked as expected")

# Test the calc_2 function you will implement above:
def test_calc_2():
    # Check wether the function that is to be tested has been defined yet:
    if not "calc_2" in globals():
        print("The function 'calc_2' that is to be tested has not been defined yet")
    else:
        # Function has been defined, so test it:
        expected_result = 12
        actual_result = calc_2()
        if expected_result != actual_result:
            print("calc_2() gave result ", actual_result, ", but expected is ", expected_result)
        else:
            print("calc_2() worked as expected")


# Test the calc_3 function you will implement above:
def test_calc_3():
    # Check wether the function that is to be tested has been defined yet:
    if not "calc_3" in globals():
        print("The function 'calc_3' that is to be tested has not been defined yet")
    else:
        # Function has been defined, so test it:
        expected_result = 9
        actual_result = calc_3()
        if expected_result != actual_result:
            print("calc_3() gave result ", actual_result, ", but expected is ", expected_result)
        else:
            print("calc_3() worked as expected")

test_calc_1()
test_calc_2()
test_calc_3()

# 9)
print("Aufgabe 9")
def inch_to_cm(a):
    return(a * 2.54)

a = 2
print(inch_to_cm(a))
b = 50
print(inch_to_cm(b))
c = 92.7
print(inch_to_cm(c))

# Test the inch_to_cm function you will implement above:
def test_inch_to_cm():
    # Check wether the function that is to be tested has been defined yet:
    if not "inch_to_cm" in globals():
        print("The function 'inch_to_cm' that is to be tested has not been defined yet")
    else:
        # Function has been defined, so test it:
        inch_argument = 5
        expected_result = 12.7
        actual_result = inch_to_cm(inch_argument)
        if expected_result != actual_result:
            print("inch_to_cm() gave result ", actual_result, ", but expected is ", expected_result)
        else:
            print("inch_to_cm() worked as expected")

test_inch_to_cm()

# 10)
# Test the inch_to_cm function you will implement above:
def test_inch_to_cm():
    # Check wether the function that is to be tested has been defined yet:
    if not "inch_to_cm" in globals():
        print("The function 'inch_to_cm' that is to be tested has not been defined yet")
    else:
        # Function has been defined, so test it:
        inch_argument_1 = 2
        expected_result_1 = 5.08
        inch_argument_2 = 50
        expected_result_2 = 127
        inch_argument_3 = 92.7
        expected_result_3 = 235.458
        actual_result_1 = inch_to_cm(inch_argument_1)
        actual_result_2 = inch_to_cm(inch_argument_2)
        actual_result_3 = inch_to_cm(inch_argument_3)
        if expected_result_1 != actual_result_1 and (expected_result_2 != actual_result_2) and (expected_result_3 != actual_result_3) :
            print("inch_to_cm() gave result ", actual_result_1,actual_result_2,actual_result_3, ", but expected is ", expected_result_1,expected_result_2,expected_result_3)
        else:
            print("inch_to_cm() worked as expected for all values")

test_inch_to_cm()
