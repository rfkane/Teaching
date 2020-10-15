a = 0
d = 1
N = 1

def sum(i):
    if i == 0:
        return 0
    else:
        return a+i*d+sum(i-1)


def g(N):
    return N/2*(2*a+(N-1)*d)


print (sum(N))
print (g(N+1))


