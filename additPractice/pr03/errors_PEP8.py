# whitespace before '('.
a = pow (base=3, exp=10)


# missing whitespace around operator.
a=pow(base=3, exp=10)


# missing whitespace after ','.
a = pow(base=3,exp=10)


# unexpected spaces around keyword / parameter equals.
a = pow(base =3, exp=10)

# expected 2 blank lines, found 1.
def getOne():
    return 1


# multiple statements on one line (colon).
if a < 4: a = getOne()


# multiple statements on one line (semicolon).
a = 1; a = 2


# comparison to None should be 'if cond is None:'.
if a == None:
    a = 1


# comparison to True should be 'if cond is True:' or 'if cond:'.
if a == True:
    a = 2