def f(P):
    return 100*+P-5*P**2

def avgslope(P,delta):
    return (f(P+delta)-f(P))/delta

print (avgslope(10,.001))



