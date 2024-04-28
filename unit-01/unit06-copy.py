

def variable(x):
    return isinstance(x, str)

def same_variable(v1,v2):
    if variable(v1) and variable(v2) and v1 == v2:
        print(f"{v1 = } is equal to { v2 = }")
        return True

def eq_number(exp, num):
    print(f"checking if {exp = } = { num = }")
    if isinstance(exp, int) or isinstance(exp, float):
        print(f"it is int or float:{exp = }")
        if exp == num:
            print(f"num is 0 and is eq to exp")
            return True

def make_sum(a1,a2):
    print(f"making Sum {a1 = } and {a2 = }\n")
    if eq_number(a1, 0):
        print(f"returning {a2 = }")
        return a2
    elif eq_number(a2, 0):
        print(f"returning {a1 = }")
        return a1
    elif isinstance(a1, int) or isinstance(a1, float) and isinstance(a2, int) or isinstance(a2, float):
        return a1 + a2
    else:
        return ["+", a1, a2]

def make_product(m1, m2):
    print(f"making product {m1=} and {m2 =} \n")
    if eq_number(m1, 0):
        return m2
    elif eq_number(m2, 0):
        print(f"returning {m1 = }")
        return m1
    elif isinstance(m1, int) or isinstance(m1, float) and isinstance(m2, int) or isinstance(m2, float):
        return m1 * m2
    else:
        return ["*", m1, m2]

def sum(x):
    print(f"checking if sum {x = }")
    if x[0] == "+":
        print(f"first item is {x[0] = }")
        return True
    else:
        return False

def addend(s):
    return s[1]

def augend(s):
    return s[2]

def product(x):
    print(f"checking if product {x = }")
    if x[0] == "*":
        print(f"first item is {x[0] = }")
        return True
    else:
        return False

def multiplier(p):
    return p[1]

def multiplicand(p):
    print(f"returning {p[2]}")
    return p[2]   

def derive(exp, var):
    print(f"deriving {exp = } and { var = }")
    if isinstance(exp, int):
        print(f"int = { exp = }")
        return int(0)
    elif isinstance(exp, float):
        print(f"float = { exp = }")
        return int(0)
    elif variable(exp):
        if same_variable(exp, var):
            print(f"same_variable = {exp = }, {var = }")
            return int(1)
        print(f"different variables = { exp = },{var = }") 
        return int(0)
    elif sum(exp):
        return make_sum(derive(addend(exp), var),
            derive(augend(exp),var))
    elif product(exp):
        first  = make_product(multiplier(exp), derive(multiplicand(exp), var))
        print(f"{first = }")
        second = make_product(derive(multiplier(exp),var), multiplicand(exp))
        print(f"{second = }")
        return make_sum(first, second)
    else:
        raise SystemExit(f"unknown expression type: DERIVE {exp}")


def main():
    #print(f'Answer 1: {derive(["+","x","3"],"x")}')
    print("\n")
    print(f"Answer 2: {derive(["*","x","y"],"x")}")
    print("\n")
    #print(f"Answer 3: {derive(["*",["*","x","y"], ["+","x","3"]],"x")}")



if __name__ == "__main__":
    main()    