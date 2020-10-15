g = .02
initialbalance = 100
years = 35

def f(i):
    if i > 0:
        return f(i-1)*(1+g)
    else:
        return initialbalance

print (f(years))
