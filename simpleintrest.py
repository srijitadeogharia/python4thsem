def simple_intrest():

    p = float(input("Enter principle:"))

    r = float(input("Enter rate of intrest:"))

    t = float(input("Enter time:"))

    si = float(p*r*t)/100

    return(si)

v = simple_intrest()
print(v)