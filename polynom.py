p = [2, 0, 1]
q = [-2, 1, 0, 0, 1]

def poly_to_string(p_list):
    # Task 1: Convert the polynomial represented by the input list of coefficients to a string
    if not p_list:
        return '0'
    if all(x == 0 for x in p_list):
        return '0'
    # Iterate through the list with enumerate to also get the index value of the contents
    output = []
    for i, c in enumerate(p_list):
        if c == 0:
            continue
        elif c > 0 and i == 0:
            output.append(str(c))
        
        elif c < 0 and i == 0:
            output.append("({})".format(str(c)))

        elif c > 1 and i == 1:
            output.append("{}x".format(str(c)))

        elif c == 1 and i == 1:
            output.append("x")
        
        elif c < -1 and i == 1:
            output.append("-{}x".format(str(-c)))
        
        elif c == -1 and i == 1:
            output.append("-x")

        elif c > 1 and i > 1:
            output.append("{}x^{}".format(str(c),str(i)))

        elif c == 1 and i > 1:
            output.append("x^{}".format(str(i)))

        elif c < -1 and i > 1:
            output.append("-{}x^{}".format(str(-c),str(i)))
        
        elif c == -1 and i > 1:
            output.append("-x^{}".format(str(i)))
            
    return ' + '.join(output)

def drop_zeros(p_list):
    # Task 2: drop any extra zeroes in the polynomial list
    result = p_list
    remove_zero = True
    # The while loop keeps going until the last number of the list is not a 0
    while remove_zero:
        if result[-1] == 0:
            result.pop()
        else:
            remove_zero = False
    return result
        
def eq_poly(p,q):
    # Task 3: Compare two polynomials and return True if they are equivalent and False otherwise
    one = poly_to_string(p)
    two = poly_to_string(q)
    # Checks if the strings are the same returns True if they are and False if they are not the same
    if one == two:
        return True
    else:
        return False

def eval_poly(p_list, x):
    # Task 4: Evaluate the polynomial represented by the input list of coefficients at the point x
    total = 0
    # Uses enumerate again to get the index value of the item in the p_list to calculate the result
    for i, c in enumerate(p_list):
        total += c * x**i
    return total

def neg_poly(p_list):
    # Task 5: Return the negation of a polynomial
    result = []
    # Iterates through p-list and multiplies each number with -1
    for c in p_list:
        result.append(c*-1)
    return result

def add_poly(p_list, q_list):
    # Task 6: Return the sum of two polynomials
    n = max(len(p_list), len(q_list))
    result = []
    # Iterates the range of the max length of the list and adds zeros to the shorter list so it matches the length of the longer list and adds them together 
    for i in range(n):
        p_coef = p_list[i] if i < len(p_list) else 0
        q_coef = q_list[i] if i < len(q_list) else 0
        result.append(p_coef + q_coef)
    return result

def sub_poly(p_list, q_list):
    #Task 7: returns subtractions of two polynomials
    n = max(len(p_list), len(q_list))
    result = []
    # Iterates the range of the max length of the list and adds zeros to the shorter list so it matches the length of the longer list and subtracts them
    for i in range(n):
        p_coef = p_list[i] if i < len(p_list) else 0
        q_coef = q_list[i] if i < len(q_list) else 0
        result.append(p_coef - q_coef)
    return result
    

x = 2
# Calling all the functions 
print(poly_to_string(p))
print(drop_zeros(p))
print(eq_poly(p,p))
print(eval_poly(p, x))
print(neg_poly(q))
print(add_poly(p,q))
print(sub_poly(p,q))