
def mymaxfunc(elements):
    m = elements[0]
    for element in elements:
        if element > m:
            m = element
    return m
